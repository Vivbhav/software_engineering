#import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")



