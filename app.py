import whisper
import streamlit as st
import warnings
import json

# Suppress the specific FutureWarning from torch
warnings.filterwarnings("ignore", category=FutureWarning, module="torch")

# Load the Whisper model without the weights_only argument
model = whisper.load_model("base")

st.title("Transcription Tool")

# Upload file using Streamlit
uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "m4a"])

def format_srt_time(seconds):
    """Format time in seconds to SRT/VTT time format."""
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02}:{int(m):02}:{int(s):02},{int((s % 1) * 1000):03}"

def write_srt(segments, file):
    """Write the transcription segments to an SRT file."""
    for idx, segment in enumerate(segments):
        start = format_srt_time(segment["start"])
        end = format_srt_time(segment["end"])
        file.write(f"{idx + 1}\n{start} --> {end}\n{segment['text']}\n\n")

def write_vtt(segments, file):
    """Write the transcription segments to a VTT file."""
    file.write("WEBVTT\n\n")
    for segment in segments:
        start = format_srt_time(segment["start"])
        end = format_srt_time(segment["end"])
        file.write(f"{start} --> {end}\n{segment['text']}\n\n")

def write_tsv(segments, file):
    """Write the transcription segments to a TSV file."""
    file.write("start\tend\ttext\n")
    for segment in segments:
        start = format_srt_time(segment["start"])
        end = format_srt_time(segment["end"])
        file.write(f"{start}\t{end}\t{segment['text']}\n")

if uploaded_file is not None:
    # Save the uploaded file locally
    file_path = uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Transcribe the audio file
    st.write("Transcribing...")
    result = model.transcribe(file_path, language="en")

    # Display the transcription
    st.write("Transcription:")
    st.write(result["text"])

    # Define the output formats
    formats = ["txt", "srt", "vtt", "json", "tsv"]

    # Save transcription to different formats
    for fmt in formats:
        output_path = f"{file_path.rsplit('.', 1)[0]}.{fmt}"
        with open(output_path, "w", encoding="utf-8") as out_file:
            if fmt == "txt":
                out_file.write(result["text"])
            elif fmt == "srt":
                write_srt(result["segments"], out_file)
            elif fmt == "vtt":
                write_vtt(result["segments"], out_file)
            elif fmt == "json":
                json.dump(result, out_file, ensure_ascii=False, indent=4)
            elif fmt == "tsv":
                write_tsv(result["segments"], out_file)

    # Provide download links for each file format
    st.write("Download Transcription Files:")
    for fmt in formats:
        output_path = f"{file_path.rsplit('.', 1)[0]}.{fmt}"
        with open(output_path, "rb") as file:
            btn = st.download_button(
                label=f"Download {fmt.upper()} file",
                data=file,
                file_name=output_path,
                mime="text/plain" if fmt in ["txt", "srt", "vtt", "tsv"] else "application/json"
            )

    # Log each phrase with start and end times
    st.write("Transcription Log:")
    for segment in result["segments"]:
        start = format_srt_time(segment["start"])
        end = format_srt_time(segment["end"])
        st.write(f"Start: {start}, End: {end}, Text: {segment['text']}")
