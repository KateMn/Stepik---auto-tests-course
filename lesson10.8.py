from selenium import webdriver
import time 
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("test@test.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))   
    file_path = os.path.join(current_dir, 'file.txt')          
    input4 = browser.find_element_by_id("file")
    input4.send_keys(file_path)


    button = browser.find_element_by_css_selector("div > form > button")
    button.click()


finally:

    time.sleep(30)

    browser.quit()

