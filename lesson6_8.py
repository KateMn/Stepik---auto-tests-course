from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    f_name = browser.find_element_by_css_selector(".first_block .first")
    f_name.send_keys("Тестуш")
    l_name = browser.find_element_by_css_selector(".first_block .second")
    l_name.send_keys("Тестовицкий")
    email = browser.find_element_by_css_selector(".first_block .third")
    email.send_keys("test@test.com")

    # Отправляем заполненную форму
    submit = browser.find_element_by_css_selector(".btn")
    submit.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

except AssertionError:
    print("Заголовок не равен 'Congratulations! You have successfully registered!'")


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()