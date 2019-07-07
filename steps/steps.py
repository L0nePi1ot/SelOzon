from behave import *

from pages.ozon_page import OzonMainPage

#page = OzonMainPage


@step('Перейти в раздел: {section_name}, подраздел {section_button_name}')
def navigation_selection(context, section_name, section_button_name):
    page = context.page
    page.click(xpath=page.CATALOG_BUTTON)
    page.navigation_selection(section_name=section_name, section_button_name=section_button_name)


@step('Установить фильтр по наименованию бренда: {brand_name}')
def select_checkbox_brand_name(context, brand_name):
    page = context.page
    page.select_checkbox_brand_name(brand_name=brand_name)


@step('Сортировать по: {sorting_method}')
def sorting_by_name(context, sorting_method):
    page = context.page
    page.sorting_by_name(sorting_method=sorting_method)


@step('Выбрать товар по номеру {value}')
def add_to_cart(context, value):
    page = context.page
    page.add_to_cart(value=value)


@step('Перейти в корзину')
def go_to_cart(context):
    page = context.page
    page.go_to_cart()


@step('Сравнить стоимость выбранного предмета и суммы корзины')
def comparison_price_and_total_amount(context):
    page = context.page
    page.comparison_price_and_total_amount()
