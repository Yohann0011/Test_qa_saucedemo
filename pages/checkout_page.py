from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def get_error_message(self):
        return self.find((By.CSS_SELECTOR, "h3[data-test='error']")).text

    def fill_info(self, first, last, zip_code):
        self.type_text(self.FIRST_NAME, first)
        self.type_text(self.LAST_NAME, last)
        self.type_text(self.POSTAL_CODE, zip_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_order(self):
        self.click(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.find(self.COMPLETE_HEADER).text