from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_obj = browser.find_element(By.ID, 'num1')
    num2_obj = browser.find_element(By.ID, 'num2')

    num1 = int(num1_obj.text)
    num2 = int(num2_obj.text)

    res = num1 + num2
    txt_res = str(res)
    print(txt_res)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(txt_res)

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
