from selenium import webdriver
import time 
import os

import math

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
  

    button = browser.find_element_by_css_selector("form > div > div > button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    span = browser.find_element_by_id("input_value")
    x = span.text
    y = calc(x)
  
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y) 
    button = browser.find_element_by_css_selector("form > div > div > button")
    button.click() 

finally:

    time.sleep(30)

    browser.quit()

