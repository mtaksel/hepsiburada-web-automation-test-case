import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from pages.PageBase import PageBase
from constants.globalconstants import *


@pytest.mark.usefixtures("setup")
class ShoppingCart(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    
    def click_increase_button(self):
        increase_buton_locate = self.wait_element_visibility(INCREASE_BUTON_LOCATE)
        increase_buton_locate.click()

    def item_quantity_assert(self):
        item_quantity_text_locate = self.wait_element_visibility(ITEM_QUANTITY_TEXT_LOCATE)
        item_quantity_value = item_quantity_text_locate.get_attribute("value")
        return item_quantity_value
    
    def click_decrease_buton(self):
        decrease_buton = self.wait_element_visibility(DECREASE_BUTON_LOCATE)
        decrease_buton.click()

    def click_rubbish_bin(self):
        rubbish_bin = self.wait_element_visibility(RUBBISH_BIN_LOCATE)
        rubbish_bin.click()

    def empty_text_assert(self):
        empty_text_locate = self.wait_element_visibility(EMPTY_TEXT_LOCATE)
        return empty_text_locate.text