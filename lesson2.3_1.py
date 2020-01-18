from selenium import webdriver
import time 
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) 

    link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

     button = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"))
    )

    button.click()
    message = browser.find_element_by_id("price")
    
    assert "100" in message.text

    button = browser.find_element_by_id("book")
    button.click() 
   
    span = browser.find_element_by_id("input_value")
    x = span.text
    y = calc(x)

    button = browser.find_element_by_id("solve")
    button.click() 
   
finally:

    time.sleep(30)

    browser.quit()

