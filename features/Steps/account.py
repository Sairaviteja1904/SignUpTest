from selenium import webdriver
from pages.signup_page import RegistrationPage
from pages.login_page import LoginPage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

@given('the user is on the sign-up page')
def open_registration_page(context):
    context.driver = webdriver.Chrome()
    context.signup_page = RegistrationPage(context.driver)
    context.signup_page.open()

@when('the user enters valid details and clicks on Create an Account button')
def registration_details(context):
    context.email = "test19043@gmail.com"
    context.signup_page.register("V", "SRT", context.email, "Password@1234")
    time.sleep(3)

@then('the user should be redirected to the Account page')
def verify_registration(context):
    assert context.signup_page.registration_successful()
    context.driver.quit()

@when('the user enters an email that is already registered')
def registration_details(context):
    context.email = "test19043@gmail.com"
    context.signup_page.register("V", "SRT", context.email, "Password@1234")

@then('the user should see an error message indicating the email already exists')
def verify_failure_message(context):
    try:
        time.sleep(5) 
        error_message_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'There is already an account with this email address')]"))
        )
        error_text = error_message_element.text
        expected_text = "There is already an account with this email address."
        assert expected_text in error_text, f"Expected '{expected_text}', but got '{error_text}'"
        print("Test Passed: Correct failure message displayed")

    except Exception as e:
        print(f"Test Failed: {str(e)}")
        assert False, "Failure message not displayed"
    context.driver.quit()

@when("the user enters a mismatched password and confirm password")
def incorrect_password_confirmation(context):
    context.signup_page.password("testuser@gmail.com", "Password123", "WrongPassword")

@then("the user should see an error message indicating that passwords do not match")
def verify_password_error(context):
    time.sleep(2) 
    assert context.signup_page.password_mismatch_error_displayed(), "Password mismatch error not displayed"
    context.driver.quit()

@when("the user enters an invalid email format")
def registration_details(context):
    context.email = "test354"
    context.signup_page.register("V", "SRT", context.email, "Password@1234")
    time.sleep(3)

@then("the user should see an error message indicating invalid email format")
def verify_invalid_email_message(context):
    assert context.signup_page.invalid_email_error_displayed(), "Invalid email error not displayed"
    context.driver.quit()

@when("the user leaves required fields (like emai or password) empty")
def skip_required_fields(context):
    context.signup_page.submit_button()

@then("the user should see an error message indicating which fields are missing")
def verify_required_fields_error(context):
    time.sleep(5)
    errors = context.signup_page.required_field_errors()
    
    expected_errors = {
        "firstname-error": "This is a required field.",
        "email_address-error": "This is a required field.",
        "password-error": "This is a required field.",
        "password-confirmation-error": "This is a required field."
    }

    for field, expected_message in expected_errors.items():
        assert field in errors and errors[field] == expected_message, f"Error for {field} not found or incorrect"
    context.driver.quit()

@when("the user enters a password that doesn’t meet the criteria")
def enter_weak_password(context):
    context.signup_page.password("testuser@gmail.com", "123456", "123456")

@then("the user should see an error message indicating that the password is weak")
def verify_weak_password_message(context):
    time.sleep(5)
    error_message = context.signup_page.weak_password_error_message()
    expected_message = "Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored."
    assert expected_message in error_message, f"Expected '{expected_message}', but got '{error_message}'"
    context.driver.quit()

@given("the user is on the login page")
def open_login_page(context):
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when('the user enters correct credentials and clicks the "Log In" button')
def login_details(context):
    context.email = "test19043@gmail.com"
    if context.email is None:
        raise ValueError("Email is not available! Ensure the registration step ran before login.")
    context.login_page.login(context.email, "Password@1234")
    time.sleep(3)

@then('the user should be redirected to the MyAccount page')
def verify_login(context):
    time.sleep(5)
    assert context.login_page.login_successful()

@when('the user enters incorrect credentials and clicks the "Log In" button')
def login_details(context):
    context.email = "test19043@gmail.com"
    context.login_page.login(context.email, "Passw")
    time.sleep(3)

@then("the user should see an error message indicating incorrect credentials")
def verify_login_failed(context):
    time.sleep(2)
    error_message = context.login_page.error_message()
    expected_message = "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
    assert expected_message in error_message, f"Expected '{expected_message}', but got '{error_message}'"
    context.driver.quit()

@when("the user clicks the Sign out button")
def logout(context):
    context.login_page.logout()

@then("the user should be Signed out and redirected to the Home page")
def verify_logout(context):
    time.sleep(10) 
    HOME_PAGE_TITLE = (By.XPATH, "//span[@class='base' and @data-ui-id='page-title-wrapper']")

    home_title = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(HOME_PAGE_TITLE)
    ).text

    assert home_title == "Home Page", f"Logout failed! Expected 'Home Page', but got '{home_title}'"
    print("Logout successful, redirected to Home Page.")


@when('the user clicks the Forgot Password button')
def request_forgot_password(context):
    context.login_page.forgot_password() 
    context.login_page.password_reset("testuser@gmail.com")

@then("the user should be redirected to Reset Password Page and redirected to the login page")
def verify_forgot_password_request(context):
    actual_message = context.driver.find_element(By.CSS_SELECTOR, "div.message-success").text
    expected_message_part = "you will receive an email with a link to reset your password"
    assert expected_message_part in actual_message, \
    f"Assertion Failed! Expected message to contain '{expected_message_part}', but got '{actual_message}'"
    context.driver.quit()