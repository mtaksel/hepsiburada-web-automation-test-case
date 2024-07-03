from selenium.webdriver.common.by import By

BASE_URL = "https://www.hepsiburada.com/"

##

HOMEPAGE_CATEGORY_BUTON = (By.CLASS_NAME, "sf-MenuItems-WulWXvlfIAwNiOUGY7FP")
SELECT_COMPUTER_CATEGORY = (By.LINK_TEXT, "Bilgisayar/Tablet")
COMPUTER_TEXT_LOCATE = (By.CLASS_NAME, "gQjF21piuOrwYvanqai8")
COMPUTER_TEXT = ("Bilgisayar Fiyatları ve Modelleri")
SELECT_SUB_CATEGORY = (By.CLASS_NAME, "sf-ChildMenuItems-KdzkrxSVhcwDy3od0Yre.item-1854")
SUB_CATEGORY_TEXT_LOCATE = (By.CLASS_NAME, "gQjF21piuOrwYvanqai8")
SUB_CATEGORY_TEXT = ("Laptop Fiyatları Notebook Modelleri")
SEARCH_BAR_LOCATE = (By.CLASS_NAME, "theme-IYtZzqYPto8PhOx3ku3c")
SEARCH_ITEM_DATA = ("oyun")
SEARCH_ITEM_MENU_LOCATE = (By.CLASS_NAME, "suggestion-bFuMEYbMcOk3K1dcDu8V")
SEARCHED_ITEM_TEXT_LOCATE = (By.CLASS_NAME, "gQjF21piuOrwYvanqai8")
SEARCHED_ITEM_TEXT = ("Oyuncak Gezegeni Hasbro Oyuncaklar")
SEARCH_BAR_LOCATE_CLICK = (By.CLASS_NAME, "searchBoxOld-M1esqHPyWSuRUjMCALPK")
ITEM_SELECT_LOCATE = (By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[3]/div/div[2]/div[3]/div/div[2]/div/div/div/div/div/div/ul/li[1]/div")
ITEM_DESC_LOCATE = (By.CSS_SELECTOR, "div.lg-3:nth-child(2) > h3:nth-child(1)")
ITEM_DESC_TEXT = 'CYBORG 15 A13VF-892XTR'
ADD_TO_CART_LOCATE = (By.ID, "addToCart")
GO_TO_CART_BUTTON_LOCATE = (By.CSS_SELECTOR, ".checkoutui-ProductOnBasketHeader-zdTSacusLu4Cu0LDpmnB > button:nth-child(1)")
ITEM_IN_CART_LOCATE = (By.CLASS_NAME, "product_name_2Klj3")
ITEM_IN_CART_TEXT = 'MSI CYBORG 15 A13VF-892XTR Intel Core i7 13620H 16GB 512GB SSD RTX4060 Freedos 15.6" FHD 144Hz Taşınabilir Bilgisayar'

##

INCREASE_BUTON_LOCATE = (By.CSS_SELECTOR, ".product_quantities_1LpFc > a:nth-child(3) > svg:nth-child(1)")
ITEM_QUANTITY_TEXT_LOCATE = (By.CSS_SELECTOR, ".product_quantities_1LpFc > input:nth-child(2)")
DECREASE_BUTON_LOCATE = (By.CSS_SELECTOR, ".product_quantities_1LpFc > a:nth-child(1) > svg:nth-child(1)")
RUBBISH_BIN_LOCATE = (By.CLASS_NAME, "trash_button_3KWju")
EMPTY_TEXT_LOCATE = (By.CSS_SELECTOR, ".content_Z9h8v > h1:nth-child(1)")
EMPTY_TEXT = "Sepetin şu an boş"