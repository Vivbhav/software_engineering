import urllib2
import urllib
from urlparse import urlparse
import re
import time
import sys
from lxml import html
from lxml.html import parse
from time import sleep
from re import findall,sub
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from HTMLParser import HTMLParser
import sys  

def youtube(String, option):
	reload(sys)  
	sys.setdefaultencoding('utf8')
	query_string = urllib.quote_plus(String)
	#print(query_string)
	#query_string = urllib.urlencode(query_string)
	#cond = input("Show all results (1) / Play Most Relevant (2)- ")
	#if option == "Show all":
	#    cond = 1
	#else:
	#    cond = 2
	html_content = urllib2.Request("http://www.youtube.com/results?search_query=" + query_string)
	#driver = webdriver.Firefox()
	#driver.get("http://www.youtube.com/results?search_query=" + query_string)
	#print(html_content)
	cont = urllib2.urlopen(html_content)
	#cont = parse(cont)
	#print(type(cont.read()))
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', cont.read().decode())
	print(search_results)
	
	driver = webdriver.Firefox()
	if int(option) == 1:
		driver.get("http://www.youtube.com/results?search_query=" + query_string) #Shows all results
	else:
		driver.get("http://www.youtube.com/watch?v=" + search_results[0]) #Plays the most relevant automatically.

if __name__ == '__main__':
	youtube(sys.arg[1])



