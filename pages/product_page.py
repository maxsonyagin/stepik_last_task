from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_to_basket(self, timeout=10):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.browser.implicitly_wait(timeout)
        self.solve_quiz_and_get_code()

    def check_item_name_equal(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_name_in_added_message = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_ADDED_MESSAGE).text
        assert item_name == item_name_in_added_message, f"Expected item name from product page to be equal" \
                                                        f" to item name in added message. Got: item name '{item_name}'" \
                                                        f" item name in added message:'{item_name_in_added_message}'"

    def check_price_equal(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        item_price_in_added_message = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_IN_ADDED_MESSAGE).text
        assert item_price == item_price_in_added_message, f"Expected item price from product page to be equal" \
                                                          f" to item price in added message. Got: item name '{item_price}'" \
                                                          f" item name in added message:'{item_price_in_added_message}'"
