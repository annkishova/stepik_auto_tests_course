from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    
    #Нажимаем забронировать
    button_book = browser.find_element_by_css_selector('#book')
    button_book.click()

    # Получить число
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    # Записать ответ
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

