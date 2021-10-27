import os

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, 'div > input:nth-child(2)')
    first_name.send_keys('Iuri')

    last_name = browser.find_element(By.CSS_SELECTOR, 'div > input:nth-child(4)')
    last_name.send_keys('Ostrikov')

    email = browser.find_element(By.CSS_SELECTOR, 'div > input:nth-child(6)')
    email.send_keys('me@iuriostrikov.com')

    send_file_btn = browser.find_element(By.ID, 'file')
    path_to_current_dir = os.path.abspath(os.path.dirname(__file__))
    path_to_file = os.path.join(path_to_current_dir, 'test.txt')
    send_file_btn.send_keys(path_to_file)

    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
