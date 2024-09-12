import streamlit as st
import whisper
import os

# Load Whisper model
model = whisper.load_model("base")

# Streamlit app title
st.title("Audio Transcription Tool")

# File uploader widget
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "m4v", "wav", "mp3"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Transcribe the audio
    st.write("Transcribing...")
    result = model.transcribe(uploaded_file.name)
    transcription = result["text"]

    # Display the transcription
    st.subheader("Transcription")
    st.text_area("Transcript", transcription, height=300)

    # Option to download the transcription
    st.download_button("Download Transcription", transcription, file_name="transcription.txt")

    # Remove the temporary file
    os.remove(uploaded_file.name)
import streamlit as st
import whisper
import os

# Load Whisper model
model = whisper.load_model("base")

# Streamlit app title
st.title("Audio Transcription Tool")

# File uploader widget
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "m4v", "wav", "mp3"])

if uploaded_file is not None:
        # Save the uploaded file temporarily
            with open(uploaded_file.name, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                            # Transcribe the audio
                                st.write("Transcribing...")
                                    result = model.transcribe(uploaded_file.name)
                                        transcription = result["text"]

                                            # Display the transcription
                                                st.subheader("Transcription")
                                                    st.text_area("Transcript", transcription, height=300)

                                                        # Option to download the transcription
                                                            st.download_button("Download Transcription", transcription, file_name="transcription.txt")

                                                                # Remove the temporary file
                                                                    os.remove(uploaded_file.name)
import streamlit as st
import whisper
import os

# Load Whisper model
model = whisper.load_model("base")

# Streamlit app title
st.title("Audio Transcription Tool")

# File uploader widget
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "m4v", "wav", "mp3"])

if uploaded_file is not None:
        # Save the uploaded file temporarily
            with open(uploaded_file.name, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                            # Transcribe the audio
                                st.write("Transcribing...")
                                    result = model.transcribe(uploaded_file.name)
                                        transcription = result["text"]

                                            # Display the transcription
                                                st.subheader("Transcription")
                                                    st.text_area("Transcript", transcription, height=300)

                                                        # Option to download the transcription
                                                            st.download_button("Download Transcription", transcription, file_name="transcription.txt")

                                                                # Remove the temporary file
                                                                    os.remove(uploaded_file.name)
import streamlit as st
import whisper
import os

# Load Whisper model
model = whisper.load_model("base")

# Streamlit app title
st.title("Audio Transcription Tool")

# File uploader widget
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "m4v", "wav", "mp3"])

if uploaded_file is not None:
        # Save the uploaded file temporarily
            with open(uploaded_file.name, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                            # Transcribe the audio
                                st.write("Transcribing...")
                                    result = model.transcribe(uploaded_file.name)
                                        transcription = result["text"]

                                            # Display the transcription
                                                st.subheader("Transcription")
                                                    st.text_area("Transcript", transcription, height=300)

                                                        # Option to download the transcription
                                                            st.download_button("Download Transcription", transcription, file_name="transcription.txt")

                                                                # Remove the temporary file
                                                                    os.remove(uploaded_file.name)

