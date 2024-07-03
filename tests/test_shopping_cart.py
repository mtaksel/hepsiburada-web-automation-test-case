from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.navbar import *
from pages.shopping_cart import *
import allure
import softest
import unittest
import pytest

@pytest.mark.usefixtures("setup")
@ddt
class TestShoppingCart(softest.TestCase, unittest.TestCase):

    def test_adding_items_to_cart(self):
        shoppingCart = ShoppingCart(self.driver)
        navbar = Navbar(self.driver)
        navbar.click_category_buton()
        navbar.hover_computer_category()
        navbar.click_sub_category()
        navbar.scroll_down()
        navbar.select_item_from_list()
        self.driver.close()
        navbar.return_first_tab()
        navbar.scroll_down()
        navbar.click_add_to_cart()
        navbar.scroll_up()
        navbar.click_go_to_cart()
        self.soft_assert(self.assertEqual,navbar.item_in_cart_assert(),ITEM_IN_CART_TEXT, "The data is not matching")
        self.assert_all()
    
    def test_increasing_item_in_shopping_cart(self):
        shoppingCart = ShoppingCart(self.driver)
        navbar = Navbar(self.driver)
        navbar.click_category_buton()
        navbar.hover_computer_category()
        navbar.click_sub_category()
        navbar.scroll_down()
        navbar.select_item_from_list()
        self.driver.close()
        navbar.return_first_tab()
        navbar.scroll_down()
        navbar.click_add_to_cart()
        navbar.scroll_up()
        navbar.click_go_to_cart()
        shoppingCart.click_increase_button()
        self.soft_assert(self.assertEqual,shoppingCart.item_quantity_assert(),"2", "The data is not matching")
        self.assert_all()

    def test_decreasing_item_in_shopping_cart(self):
        shoppingCart = ShoppingCart(self.driver)
        navbar = Navbar(self.driver)
        navbar.click_category_buton()
        navbar.hover_computer_category()
        navbar.click_sub_category()
        navbar.scroll_down()
        navbar.select_item_from_list()
        self.driver.close()
        navbar.return_first_tab()
        navbar.scroll_down()
        navbar.click_add_to_cart()
        navbar.scroll_up()
        navbar.click_go_to_cart()
        shoppingCart.click_increase_button()
        self.soft_assert(self.assertEqual,shoppingCart.item_quantity_assert(),"2", "The data is not matching")
        self.assert_all()
        shoppingCart.click_decrease_buton()
        self.soft_assert(self.assertEqual,shoppingCart.item_quantity_assert(),"1", "The data is not matching")
        self.assert_all()
    
    def test_removing_item_in_the_shopping_cart(self):
        shoppingCart = ShoppingCart(self.driver)
        navbar = Navbar(self.driver)
        navbar.click_category_buton()
        navbar.hover_computer_category()
        navbar.click_sub_category()
        navbar.scroll_down()
        navbar.select_item_from_list()
        self.driver.close()
        navbar.return_first_tab()
        navbar.scroll_down()
        navbar.click_add_to_cart()
        navbar.scroll_up()
        navbar.click_go_to_cart()
        shoppingCart.click_increase_button()
        self.soft_assert(self.assertEqual,shoppingCart.item_quantity_assert(),"2", "The data is not matching")
        self.assert_all()
        shoppingCart.click_rubbish_bin()
        self.soft_assert(self.assertEqual,shoppingCart.empty_text_assert(),EMPTY_TEXT, "The data is not matching")
        self.assert_all()

