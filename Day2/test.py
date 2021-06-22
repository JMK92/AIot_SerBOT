from gtts import gTTS
import subprocess

text = "시작합니다."
filename = "en_tts.mp3"

tts = gTTs(text, lang='ko') 
tts.save(filename)

with subprocess.Popen(['play', 'en_tts.mp3']) as p: #Popen([리눅스 명령어, filename])
    p.wait()
