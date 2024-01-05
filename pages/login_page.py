from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException
import time


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.implicitly_wait(10)
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD1_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2_FIELD).send_keys(password)
        time.sleep(2)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, f"Url {self.browser.current_url} does not contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register Form is not presented"

