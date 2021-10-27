import math
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def calc(x1):
    return str(math.log(abs(12 * math.sin(int(x1)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price_value = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), str(100))
    )

    btn_book = browser.find_element(By.ID, 'book')
    btn_book.click()

    input_value_obj = browser.find_element(By.ID, 'input_value')
    input_value = input_value_obj.text

    result = calc(input_value)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)

    send_btn = browser.find_element(By.ID, 'solve')
    send_btn.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(100)
    # закрываем браузер после всех манипуляций
    browser.quit()
