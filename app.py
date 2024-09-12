import whisper
import streamlit as st
import warnings

# Suppress the specific FutureWarning from torch
warnings.filterwarnings("ignore", category=FutureWarning, module="torch")

# Load the Whisper model
model = whisper.load_model("base", weights_only=True)

st.title("Transcription Tool")

# Upload file using Streamlit
uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "m4a"])

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
                whisper.utils.write_srt(result["segments"], out_file)
            elif fmt == "vtt":
                whisper.utils.write_vtt(result["segments"], out_file)
            elif fmt == "json":
                import json
                json.dump(result, out_file, ensure_ascii=False, indent=4)
            elif fmt == "tsv":
                whisper.utils.write_tsv(result["segments"], out_file)

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
