# mytts

first detach the audio part from your video
```bash
ffmpeg -i path/to/video/file.m4v -vn -acodec pcm_s16le -ar 44100 -ac 2 path/to/audio/audio.wav
```

use the local script to transcribe your audio
```
python3 local_transcribe.py audio.wav
```

if you want to use the bash command
```
whisper output.wav --model base --language en
```

you can also use the app.py with streamlit (locally) to get the transcription done
you'll get all those formats: 
```
["txt", "srt", "vtt", "json", "tsv"]
```

## run the app

```bash
# activate the virtual environement
 source myenv/bin/activate
# the launch the streamlit app
streamlit run app.py
```
