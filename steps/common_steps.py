import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.ozon_page import OzonMainPage


@given('Открыть сайт "{url}"')
def step(context, url):

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    context.driver = webdriver.Chrome(executable_path='C:/Python/webdrivers/chromedriver.exe',
                                      chrome_options=chrome_options)
    context.driver.maximize_window()
    context.driver.get(url)

    context.page = OzonMainPage(driver=context.driver)
    time.sleep(2)