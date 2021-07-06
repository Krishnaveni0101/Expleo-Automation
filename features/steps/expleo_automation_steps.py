import time

from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launch_chrome_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('open DOM website')
def open_website_url(context):
    time.sleep(5)
    context.driver.get("https://the-internet.herokuapp.com/challenging_dom")


@then('verify DOM website is launched successfully')
def verify_website_load(context):
    time.sleep(5)
    is_displayed = context.driver.find_element_by_xpath("//div[@class='example']/h3[contains(text(),"
                                                        "'Challenging DOM')]").is_displayed()
    assert is_displayed is True


@then('close browser')
def close_browser(context):
    context.driver.close()
