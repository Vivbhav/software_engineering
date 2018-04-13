"""
The core of the Intelligent Personal Assistant

Finds keywords in the input sentence,
then calls the appropriate functions.
"""

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import poem
import sentiment
#import vlc
import os
"""from Speech import speak
from files import open_folder
import firefox
from playmovie import fn_movie, fn_close_movie
from songs import fn_play_song, fn_close_song
from pdf import fn_open_pdf, fn_close_pdf
import time, datetime
import reminder
import terminal
from converse import converse
from confirm import confirm
from open_file import open_site
import subprocess
import event"""
def main_code(string):
    """
    Searches the input string for keywords, or commands.
    If keywords are found, it calls appropriate function.
    List of functions:
    (1) Open (website, pdf, folder, terminal, reminder)
    (2) Play (movies, songs)
    (3) Tell the time.
    (4) Google, or search for a string online.
    (5) Close (tab, song, movie, pdf)
    (6) Mail (read, send)
    (7) Shutdown
    (8) Reminder
    """
    #Splitting each sentence in a list of words.
    word_list = word_tokenize(string)

    #Setting up stop_words: words that are redundant.
    stop_words = set(stopwords.words('english'))

    #Creating space for a list of sentences without stop_words.

    ans = 0
    if "search" not in word_list and "google" not in word_list:
        filtered_sentence = [w for w in word_list if not w in stop_words]
    else:
        filtered_sentence = [w for w in word_list]
   
    if 'google' in filtered_sentence:
	return ("google", 40)     ## to call google function
    elif 'youtube' in filtered_sentence:
        #print ("inside youtube in maincode")
        #works = os.system('python3 youtube.py ' + "cricket")    
        return ("works", 70)
    elif 'show' in filtered_sentence:
        if 'events' in filtered_sentence:
            return ("show", 60)
    elif 'sentiment' in filtered_sentence:
        if 'analysis' in filtered_sentence:
            #ans = sentiment.sentiment_analysis(string)
            return ("sentiment", 50)
    elif 'event' in filtered_sentence:
        if 'create' in filtered_sentence:
            return ("create", 1)
        elif 'delete' in filtered_sentence:
            return ("delete", 10)
        elif 'modify' in filtered_sentence:
            return ("modify", 20)
    if 'poem' in filtered_sentence:
        data  = poem.poem()
        return (data, 0)
    if 'send' in filtered_sentence:
        if 'mail' or 'email' in filtered_sentence:
            return ("send email", 30)
    else:
        return ("Sorry, can't process your request. Please try something else.", 0)

