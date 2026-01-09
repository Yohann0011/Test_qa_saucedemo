from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_CONTAINER = (By.CLASS_NAME, "product_sort_container")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK)

    def remove_backpack_from_cart(self):
        self.click(self.REMOVE_BACKPACK)

    def get_cart_count(self):
        try:
            return self.find(self.CART_BADGE).text
        except:
            return "0"

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)

    def sort_by_name_a_to_z(self):
        self.click(self.SORT_CONTAINER)
        self.driver.find_element(By.XPATH, "//option[@value='az']").click()

    def get_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [el.text for el in elements]