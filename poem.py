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
import pyttsx3

def poem():
	driver = webdriver.PhantomJS() #For Visible window use Firefox
	driver.get('https://www.poets.org/poetsorg/poem-day')
	time.sleep(2)
	header = driver.find_elements_by_xpath("//*[@id='page-title']")[1].text
	content = driver.find_element_by_tag_name('pre').text
	out = header+"\n"+content
	driver.close()
	return(out)
