from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 

import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    span = browser.find_element_by_id("num1")
    x = span.text
    span = browser.find_element_by_id("num2")
    y = span.text
   
    result = str(int(x) + int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)
    button = browser.find_element_by_css_selector("div > form > button")
    button.click()


finally:

    time.sleep(30)

    browser.quit()

