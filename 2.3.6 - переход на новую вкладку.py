import math
import os

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def calc(x1):
    return str(math.log(abs(12 * math.sin(int(x1)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn_modal = browser.find_element(By.TAG_NAME, 'button')
    btn_modal.click()

    current_window = browser.current_window_handle

    next_window = browser.window_handles[1]
    browser.switch_to.window(next_window)

    input_value_obj = browser.find_element(By.ID, 'input_value')
    input_value = input_value_obj.text

    result = calc(input_value)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)

    send_btn = browser.find_element(By.CLASS_NAME, 'btn')
    send_btn.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
