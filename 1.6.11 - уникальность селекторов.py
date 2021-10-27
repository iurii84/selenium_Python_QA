from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    first_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input')
    first_name.send_keys("Ivan")
    name = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input')
    name.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input')
    email.send_keys("Smolensk@abrakadabra.com")


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()