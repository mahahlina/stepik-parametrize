from selenium import webdriver
import pytest
from selenium.common.exceptions import NoSuchElementException







def test_check_good_avaliable(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary btn-add-to-basket"]'), "Кнопка Добавить не найдена"

