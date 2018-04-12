import speech_recognition as sr
from time import ctime
import time
import os
#from gtts import gTTS
#import pyttsx3
import pyttsx

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def speak1(audioString):
    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait

def speak2(audioString):
    engine = pyttsx.init()
    engine.say(audioString)
    engine.runAndWait()

speak2("my name is vivek")
