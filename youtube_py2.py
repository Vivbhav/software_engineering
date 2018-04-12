import urllib2
import urllib
from urlparse import urlparse
import re
import time
import sys
from lxml import html
from time import sleep
from re import findall,sub
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

#query = urlparse(raw_input())
query_string = urllib.quote_plus(raw_input())
#print(query)
#query_string = urllib.urlencode(query)
cond = input("Show all results (1) / Play Most Relevant (2)- ")
html_content = urllib2.urlopen("http://www.youtube.com/results?" + query_string)
html = html_content.read()
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

driver = webdriver.Firefox()
if int(cond) == 1:
    driver.get("http://www.youtube.com/results?search_query=" + query_string) #Shows all results
else:
    driver.get("http://www.youtube.com/watch?v=" + search_results[0]) #Plays the most relevant automatically.


