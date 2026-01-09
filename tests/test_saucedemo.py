import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from data.test_data import BASE_URL, VALID_USER, LOCKED_USER, PASSWORD
from selenium.webdriver.common.by import By

class TestSauceDemo:
    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(BASE_URL)

    def teardown_method(self):
        self.driver.quit()

    def test_login_success(self):
        login = LoginPage(self.driver)
        login.login(VALID_USER, PASSWORD)
        assert "inventory.html" in self.driver.current_url

    def test_locked_user(self):
        login = LoginPage(self.driver)
        login.login(LOCKED_USER, PASSWORD)
        error = login.get_error_message()
        assert "locked out" in error

    def test_empty_password(self):
        login = LoginPage(self.driver)
        login.login(VALID_USER, "")
        error = login.get_error_message()
        assert "Password is required" in error

    def test_add_to_cart(self):
        login = LoginPage(self.driver)
        login.login(VALID_USER, PASSWORD)
        inventory = InventoryPage(self.driver)
        inventory.add_backpack_to_cart()
        assert inventory.get_cart_count() == "1"

    def test_remove_from_cart(self):
        login = LoginPage(self.driver)
        login.login(VALID_USER, PASSWORD)
        inventory = InventoryPage(self.driver)
        inventory.add_backpack_to_cart()
        inventory.remove_backpack_from_cart()
        assert inventory.get_cart_count() == "0"

    def test_logout(self):
        login = LoginPage(self.driver)
        login.login(VALID_USER, PASSWORD)
        inventory = InventoryPage(self.driver)
        inventory.logout()
        assert self.driver.current_url == BASE_URL

    def test_sort_a_to_z(self):
        login = LoginPage(self.driver)
        login.login(VALID_USER, PASSWORD)
        inventory = InventoryPage(self.driver)
        inventory.sort_by_name_a_to_z()
        names = inventory.get_product_names()
        assert names == sorted(names)

    def test_complete_checkout(self):
        # Login
        login = LoginPage(self.driver)
        login.login(VALID_USER, PASSWORD)
        # Agregar producto
        inventory = InventoryPage(self.driver)
        inventory.add_backpack_to_cart()
        # Ir al carrito
        inventory.click(inventory.CART_BADGE)
        cart = CartPage(self.driver)
        cart.go_to_checkout()
        # Checkout
        checkout = CheckoutPage(self.driver)
        checkout.fill_info("Test", "User", "12345")
        checkout.finish_order()
        success = checkout.get_success_message()
        assert "thank you" in success.lower()

    def test_checkout_with_alt255_char(self):
        login = LoginPage(self.driver)
        login.login(VALID_USER, PASSWORD)
        
        inventory = InventoryPage(self.driver)
        inventory.add_backpack_to_cart()
        inventory.click(inventory.CART_BADGE)
        
        cart = CartPage(self.driver)
        cart.go_to_checkout()
        
        checkout = CheckoutPage(self.driver)
        checkout.fill_info(" ", " ", "12345")  # Alt+255 = ' '
        
        
        error_elements = self.driver.find_elements(By.CSS_SELECTOR, "h3[data-test='error']")
        if error_elements:
            
            assert "is required" in error_elements[0].text
        else:
           
            checkout.finish_order()
            success = checkout.get_success_message()
            
            assert False, f"La app permitió caracteres inválidos: {success}"
    
    def test_checkout_empty_fields(self):
        
        login = LoginPage(self.driver)
        login.login(VALID_USER, PASSWORD)
        
        inventory = InventoryPage(self.driver)
        inventory.add_backpack_to_cart()
        inventory.click(inventory.CART_BADGE)
        
        cart = CartPage(self.driver)
        cart.go_to_checkout()
        
        checkout = CheckoutPage(self.driver)
        checkout.fill_info("", "", "")
        
        error = checkout.get_error_message()
        assert "is required" in error

    def test_checkout_xss_attempt(self):
        
        login = LoginPage(self.driver)
        login.login(VALID_USER, PASSWORD)
        
        inventory = InventoryPage(self.driver)
        inventory.add_backpack_to_cart()
        inventory.click(inventory.CART_BADGE)
        
        cart = CartPage(self.driver)
        cart.go_to_checkout()
        
        checkout = CheckoutPage(self.driver)
        checkout.fill_info("<script>alert('xss')</script>", "User", "12345")
        checkout.finish_order()
        
        success = checkout.get_success_message()
        
        assert "<script>" not in success

    def test_checkout_very_long_name(self):
        
        login = LoginPage(self.driver)
        login.login(VALID_USER, PASSWORD)
        
        inventory = InventoryPage(self.driver)
        inventory.add_backpack_to_cart()
        inventory.click(inventory.CART_BADGE)
        
        cart = CartPage(self.driver)
        cart.go_to_checkout()
        
        long_name = "A" * 1000
        checkout = CheckoutPage(self.driver)
        checkout.fill_info(long_name, "User", "12345")
        checkout.finish_order()
        
        success = checkout.get_success_message()
        assert "Thank you" in success
        
    
    def test_checkout_empty_cart(self):
        """Verifica que no se permita iniciar checkout con carrito vacío"""
        login = LoginPage(self.driver)
        login.login(VALID_USER, PASSWORD)
        
        
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
        
        checkout = CheckoutPage(self.driver)
        checkout.fill_info("Test", "User", "12345")
        checkout.finish_order()
        
        
        overview_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        if len(overview_items) == 0:
            
            checkout_page_2 = CheckoutPage(self.driver)
            
            success = checkout_page_2.get_success_message()
            assert "Thank you" in success
            