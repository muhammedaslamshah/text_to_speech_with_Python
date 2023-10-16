'''
This is text to speech project, using google test to speech api gTTs
'''
from gtts import gTTS
import os

text = 'hi, welcome to python text to speech'
output = gTTS(text=text, lang='en', slow=False)
output.save("text_to_speech.mp3")
