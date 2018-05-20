import gtts
import gTTs
import os

mytext = 'hello everybody welcome to my world'

language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.sava("chilla.mp3")

os.system("mpg321 chilla.mp3")