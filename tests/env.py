from selenium import webdriver
from pages.login_page import LoginPage


def before_all(context):
    context.user_email = None

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context.driver)
    
def after_scenario(context, scenario):
    context.driver.quit()