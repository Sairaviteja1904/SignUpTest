from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
import time
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/login/"
    
    EMAIL = (By.ID, "email")
    email_input = (By.ID, "email_address")
    PASSWORD = (By.ID, "pass")
    LOGIN_BUTTON = (By.ID, "send2")
    DASHBOARD = (By.XPATH, "//span[@class='base' and @data-ui-id='page-title-wrapper']")
    ACCOUNT_MENU = (By.XPATH, "//button[contains(@class, 'switch')]")
    LOGOUT_LINK = (By.XPATH, "//a[contains(text(),'Sign Out')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".message-error")
    FORGOT_PASSWORD_URL = "https://magento.softwaretestingboard.com/customer/account/forgotpassword/"
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".message-success")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.action.submit.primary")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot Your Password?")

    def open(self):
        self.driver.get(self.URL)
    
    def login(self, email, password):
        self.enter_text(*self.EMAIL, email)
        self.enter_text(*self.PASSWORD, password)
        self.click(*self.LOGIN_BUTTON)
    
    def login_successful(self):
        time.sleep(3)
        try:
            element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.DASHBOARD)
            )
            return element.text.strip() == "My Account"  
        except Exception as e:
            self.driver.save_screenshot("login_debug.png")
            print(f"Login failed: {e}")  
            return False
        
    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ACCOUNT_MENU)
        ).click()
        print("Clicked account menu.")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        ).click()
        print("Clicked logout link.")

        time.sleep(10) 

    def error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
    

    def forgot_password_page(self):
        self.driver.get(self.forgot_password_url)

    def forgot_password(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FORGOT_PASSWORD_LINK)
        ).click()

    def password_reset(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.email_input)
        ).send_keys(email)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        ).click()

    def success_message(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text
