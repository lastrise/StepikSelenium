import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

browser = webdriver.Chrome()
browser.implicitly_wait(5)


def calc(x: str):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser.get(link)

    WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    value = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.CSS_SELECTOR, "input").send_keys(value)

    button = browser.find_elements(By.CSS_SELECTOR, "button.btn")[1]
    button.click()

    print("Все хорошо")
    time.sleep(3)

finally:
    print("Все плохо")
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    browser.quit()
    # закрываем браузер после всех манипуляций

