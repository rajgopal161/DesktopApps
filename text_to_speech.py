from gtts import gTTS
import os

filee = open('test.txt', 'r').read()

text = "Hey there, wassup!"
output = gTTS(text= filee, lang='en', slow=False)
output.save('output.mp3')

os.system("start output.mp3")