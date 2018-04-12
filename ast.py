#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import urllib.request
import urllib.parse
import re
import time
from lxml import html
from time import sleep
from re import findall,sub
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import pyttsx3
 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def speak1(audioString):
    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait

 
 
def pi(data):
    if "how are you" in data:	
        speak("I am fine")
 
    if "what time is it" in data:
        speak(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Sir, I will show you where " + location + " is.")
        os.system("google-chrome https://www.google.nl/maps/place/" + location + "/&amp;")

    if "feeling down" in data:	
        speak("Why so? may I suggest listening to music, watching videos, browsing facebook or links to some coding websites?")

    if "music" or "song" in data:	
        speak("Very well. On it.")
        speak("What kind of Music?")
        mustype = urllib.parse.urlencode({"search_query" : input()})
        query_string = mustype
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        driver = webdriver.Firefox()
        driver.get("http://www.youtube.com/watch?v=" + search_results[0])


 
# initialization
time.sleep(2)
speak("Hello Sir, what can I do for you?")
while 1:
    data = input()
    pi(data)

