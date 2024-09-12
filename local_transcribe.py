import whisper
import sys

# Check if the filename is passed as an argument
if len(sys.argv) < 2:
    print("Usage: python3 transcribe.py <audiofile>")
    sys.exit(1)

# Get the filename from the command-line arguments
audio_file = sys.argv[1]

# Load the Whisper model
model = whisper.load_model("base", weights_only=True)

# Transcribe the audio file
result = model.transcribe(audio_file, language="en")

# Print the transcription result
print(result["text"])

