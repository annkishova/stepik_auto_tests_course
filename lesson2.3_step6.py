from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element_by_css_selector('button')
    button.click()
    # Переключиться на вкладку
    browser.switch_to.window(browser.window_handles[1])
    
    
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

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()