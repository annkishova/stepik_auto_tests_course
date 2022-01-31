from selenium import webdriver
import pytest
import time
 
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_chech_button_on_page(browser):
        browser.get(link)
        
        #наличие кнопки добавления в корзину
        assert browser.find_element_by_css_selector(".btn-add-to-basket"), "Кнопка не найдена"
