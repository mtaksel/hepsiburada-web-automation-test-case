import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from pages.PageBase import PageBase
from constants.globalconstants import *


@pytest.mark.usefixtures("setup")
class Navbar(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_category_buton(self):
        category_buton = self.wait_element_visibility(HOMEPAGE_CATEGORY_BUTON)
        category_buton.click()

    def click_computer_category(self):
        computer = self.wait_element_visibility(SELECT_COMPUTER_CATEGORY)
        computer.click()
    
    def computer_assert(self):
        computer_text = self.wait_element_visibility(COMPUTER_TEXT_LOCATE)
        return computer_text.text
    
    def hover_computer_category(self):
        computer_hover = self.hover(SELECT_COMPUTER_CATEGORY)


    def click_sub_category(self):
        sub_cat = self.wait_element_visibility(SELECT_SUB_CATEGORY)
        sub_cat.click()

    def sub_category_assert(self):
        sub_cat_text = self.wait_element_visibility(SUB_CATEGORY_TEXT_LOCATE)
        return sub_cat_text.text
    
    def click_search_bar(self):
        click_search_Bar = self.wait_element_visibility(SEARCH_BAR_LOCATE_CLICK)
        click_search_Bar.click()


    def search_item(self):
        search_box = self.wait_element_visibility(SEARCH_BAR_LOCATE)
        search_box.send_keys(SEARCH_ITEM_DATA)

    def click_searched_item_from_menu(self):
        search_item = self.wait_element_visibility(SEARCH_ITEM_MENU_LOCATE)
        search_item.click()
    
    def searched_item_assert(self):
        searched_item_locate = self.wait_element_visibility(SEARCHED_ITEM_TEXT_LOCATE)
        return searched_item_locate.text
    
    def select_item_from_list(self):
        item_locate1 = self.wait_element_visibility(ITEM_SELECT_LOCATE)
        item_locate1.click()

    def item_description_assert(self):
        item_desc = self.wait_element_visibility(ITEM_DESC_LOCATE)
        return item_desc.text

    def scroll_down(self):
        self.driver.execute_script("scrollBy(0,800)")

    def scroll_up(self):
        self.driver.execute_script("scrollBy(0,-800)")
    
    def return_first_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_add_to_cart(self):
        cart_locate = self.wait_element_visibility(ADD_TO_CART_LOCATE)
        cart_locate.click()

    def click_go_to_cart(self):
        gotocart_locate = self.wait_element_visibility(GO_TO_CART_BUTTON_LOCATE)
        gotocart_locate.click()
    
    def item_in_cart_assert(self):
        item_in_cart_locate = self.wait_element_visibility(ITEM_IN_CART_LOCATE)
        return item_in_cart_locate.text

        