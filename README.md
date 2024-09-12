# mytts

first detach the audio part from your video
```bash
ffmpeg -i path/to/video/file.m4v -vn -acodec pcm_s16le -ar 44100 -ac 2 path/to/audio/audio.wav
```

use the local script to transcribe your audio
```
python3 transcribe.py audio.wav
```

if you want to use the bash command
```
whisper output.wav --model base --language en
```
