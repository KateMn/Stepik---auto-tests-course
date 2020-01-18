from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_class_name("form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.third")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_css_selector("form > div.second_block > div.form-group.first_class > input")
    input4.send_keys("Russia")
    input5 = browser.find_element_by_css_selector("div > form > div.second_block > div.form-group.second_class > input")
    input5.send_keys("Russia")
    button = browser.find_element_by_xpath("/html/body/div/form/button")
    button.click()

finally:

    time.sleep(30)

    browser.quit()

