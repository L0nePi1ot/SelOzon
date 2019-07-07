import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.ozon_page import OzonMainPage


def test_ozon():

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(
        executable_path='G:/Projects/SelOzon/webdrivers/chromedriver.exe',
        chrome_options=chrome_options)
    driver.maximize_window()

    driver.get('https://ozon.ru')
    page = OzonMainPage(driver=driver)

    # Открытие каталога продуктов
    page.click(xpath=page.CATALOG_BUTTON)

    # Переход в раздел "Электроника", далее "Смартфоны"
    page.navigation_selection(section_name='Электроника', section_button_name='Смартфоны')

    # Установка фильтра на бренд "Samsung"
    page.select_checkbox_brand_name(brand_name='Samsung')

    # Сортировка цены по убыванию
    page.sorting_by_name('Сначала дорогие')

    page.add_to_cart(value='0')
    page.click(xpath=page.ADD_TO_CART)
    page.go_to_cart()

    page.comparison_price_and_total_amount()
    time.sleep(15)
