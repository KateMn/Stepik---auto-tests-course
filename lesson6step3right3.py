# coding: utf-8
# -*- coding: utf8 -*-
from selenium import webdriver
import time
import math 

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element_by_link_text("�str(math.ceil(math.pow(math.pi, math.e)*10000))")
    link.click()

finally:
    
    time.sleep(30)
 
    browser.quit()

