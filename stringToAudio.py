from gtts import gTTS
# pip install gtts

from playsound import playsound
# pip install playsound

audio = 'speech.mp3'
language = 'en'

sp = gTTS(text = 'text to be converted to audio file',
          lang = language, slow=False

          )

sp.save(audio)
playsound(audio)