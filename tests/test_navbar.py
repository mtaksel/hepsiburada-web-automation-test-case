from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.navbar import *
import allure
import softest
import unittest
import pytest

@pytest.mark.usefixtures("setup")
@ddt
class TestNavBar(softest.TestCase, unittest.TestCase):

    def test_listing_by_category(self):
        navbar = Navbar(self.driver)
        navbar.click_category_buton()
        navbar.click_computer_category()
        self.soft_assert(self.assertEqual,navbar.computer_assert(),COMPUTER_TEXT, "The data is not matching")
        self.assert_all()

    def test_listing_by_sub_category(self):
        navbar = Navbar(self.driver)
        navbar.click_category_buton()
        navbar.hover_computer_category()
        navbar.click_sub_category()
        self.soft_assert(self.assertEqual,navbar.sub_category_assert(),SUB_CATEGORY_TEXT, "The data is not matching")
        self.assert_all()

    def test_searching_and_filtering_items(self):
        navbar = Navbar(self.driver)
        navbar.click_search_bar()
        navbar.search_item()
        navbar.click_searched_item_from_menu()
        self.soft_assert(self.assertEqual,navbar.searched_item_assert(),SEARCHED_ITEM_TEXT, "The data is not matching")
        self.assert_all()

    def test_viewing_product_details(self):
        navbar = Navbar(self.driver)
        navbar.click_category_buton()
        navbar.hover_computer_category()
        navbar.click_sub_category()
        navbar.scroll_down()
        navbar.select_item_from_list()
        self.driver.close()
        navbar.return_first_tab()
        navbar.scroll_down()
        navbar.scroll_down()
        self.soft_assert(self.assertEqual,navbar.item_description_assert(),ITEM_DESC_TEXT, "The data is not matching")
        self.assert_all()

    