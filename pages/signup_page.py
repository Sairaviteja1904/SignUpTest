from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/create/"
    
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[title='Create an Account']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "message-success")
    ERROR_MESSAGE = (By.ID, "password-confirmation-error")
    EMAIL_ERROR_MESSAGE = (By.ID, "email_address-error")
    REQUIRED_FIELD_ERRORS = (By.CSS_SELECTOR, ".mage-error")
    WEAK_PASSWORD_ERROR_MESSAGE = (By.ID, "password-error")

    def open(self):
        self.driver.get(self.URL)
    
    def register(self, first_name, last_name, email, password):
        self.enter_text(*self.FIRST_NAME, first_name)
        self.enter_text(*self.LAST_NAME, last_name)
        self.enter_text(*self.EMAIL, email)
        self.enter_text(*self.PASSWORD, password)
        self.enter_text(*self.CONFIRM_PASSWORD, password)
        self.click(*self.SUBMIT_BUTTON)

    def password(self, email, password, confirm_password):
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(confirm_password)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def registration_successful(self):
        return self.find_element(*self.SUCCESS_MESSAGE).is_displayed()
    
    def submit_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def required_field_errors(self):
        errors = self.driver.find_elements(*self.REQUIRED_FIELD_ERRORS)
        return {error.get_attribute("id"): error.text for error in errors}
    
    def password_mismatch_error_displayed(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).is_displayed()
    
    def invalid_email_error_displayed(self):
        return self.driver.find_element(*self.EMAIL_ERROR_MESSAGE).is_displayed()
    
    def weak_password_error_message(self):
        return self.driver.find_element(*self.WEAK_PASSWORD_ERROR_MESSAGE).text