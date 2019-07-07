from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, xpath: str):
        """Метод получения веб элемента по xpath

        Args:
            xpath: xpath

        Returns:
            element: веб-элемент
        """
        try:
            element = WebDriverWait(driver=self.driver, timeout=20).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            element = self.driver.find_element(By.XPATH, xpath)
        return element

    def wait_clickable_element(self, xpath: str):
        """Метод проверки элемента на кликабильность

        :param xpath: xpath
        """
        element = WebDriverWait(driver=self.driver, timeout=20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath)))

        return element

    def click(self, xpath):
        """Метод для нажатия на элемент

        :param xpath: xpath
        """
        element = self.get_element(xpath=xpath)
        element.click()

    def fill_input(self, xpath, value):
        """Метод заполняет поле

        Args:
            xpath: xpath
            value: значение которым заполняется

        Returns:

        """
        element = self.get_element(xpath=xpath)
        element.send_keys(value)

    def clear_input(self, xpath):
        """Метод очистки поля ввода

        :param xpath: xpath
        """
        cleaner = self.get_element(xpath=xpath)
        cleaner.clear()

    def element_hover(self, xpath):
        """Метод наведения курсора мыши элемент

        :param xpath: xpath
        """

        element = self.wait_clickable_element(xpath=xpath)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).click().perform()

    def click_section_by_name(self, section_name: str):
        """Метод нажатия кнопки на сайте, с определенным текстом

        :param button_name: Текст на кнопке
        """
        xpath = self.SECTION_BUTTON.format(section_name=section_name)
        self.get_element(xpath=xpath)
        self.click(xpath=xpath)

    def quit_browser(self):
        """Метод закрытия браузера

        """
        self.driver.quit()

    def time_sleeper(self, value: int):
        """Вспомогательный таймер для написания тестов (Не использовать в готовом коде!!!)

        :param value: секунд
        """
        time.sleep(value)

    def navigation_selection(self, section_name, section_button_name):
        """ Навикация по разделам

        :param section_name: Основной раздел
        :param section_button_name: Подраздел
        """

        xpath_menu = self.CATALOG_SECTION.format(section_name=section_name)
        xpath_button = self.CATALOG_SECTION_BUTTON.format(section_button_name=section_button_name)
        add = self.driver.find_element(By.XPATH, xpath_menu)
        hover = ActionChains(self.driver).move_to_element(add)
        hover.perform()
        section_button = self.driver.find_element(By.XPATH, xpath_button)
        section_button.click()

    def select_checkbox_brand_name(self, brand_name):
        """Установить фильтр на бренд


        :param brand_name: Наименование бренда
        """
        scroll_page = self.driver.find_element(By.XPATH, self.FILTER_BLOCK_BRAND)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_page)

        try:
            show_all_brands = self.driver.find_element(By.XPATH, self.SHOW_ALL_BRANDS)
            ActionChains(self.driver).move_to_element(show_all_brands).click().perform()

        except Exception:
            pass

        search_input = self.get_element(xpath=self.SEARCH_BRAND_INPUT)
        search_input.clear()
        search_input.send_keys(brand_name)

        xpath = self.CHECKBOX_BRAND_NAME.format(brand_name=brand_name)
        brand_checkbox = self.driver.find_element(By.XPATH, xpath)
        ActionChains(self.driver).move_to_element(brand_checkbox).click().perform()

        time.sleep(5)

    def sorting_by_name(self, sorting_method):
        """Соритровать по указанному методу


        :param sorting_method: Метод сортировки
        """

        scroll_page = self.driver.find_element(By.XPATH, self.SORTING_SELECT)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_page)

        sort_select = self.driver.find_element(By.XPATH, self.SORTING_SELECT)
        ActionChains(self.driver).move_to_element(sort_select).click().perform()

        sort_by = self.SORTING_BY_NAME.format(sorting_method=sorting_method)
        sort_method = self.driver.find_element(By.XPATH, sort_by)
        ActionChains(self.driver).move_to_element(sort_method).click().perform()

        time.sleep(5)

    def add_to_cart(self, value):
        """Добавить элемент в корзину


        :param value: Порядковый номер элемента каталлога
        """
        xpath = self.ADD_TO_CART.format(value=value)
        scroll_page = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_page)

        global item_price
        item_price_xpath = self.ITEM_SCAN_PRICE.format(value=value)
        item_price = self.driver.find_element(By.XPATH, item_price_xpath).text

        button_add_to_cart = self.driver.find_element(By.XPATH, xpath)
        ActionChains(self.driver).move_to_element(button_add_to_cart).click().perform()

    def go_to_cart(self):
        """Переход в корзину


        """
        scroll_page = self.driver.find_element(By.XPATH, self.CART)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_page)
        button_cart = self.driver.find_element(By.XPATH, self.CART)
        ActionChains(self.driver).move_to_element(button_cart).click().perform()
        time.sleep(5)
        global cart_total_amount
        cart_total_amount = self.driver.find_element(By.XPATH, '//span[@class="price"]//span[@class="main"]').text

    def total_amount(self):
        """Получение стоимости в корзине


        """
        global cart_total_amount
        cart_total_amount = self.driver.find_element(By.XPATH, '//div[@data-test-id="total-price-block"]').text

    def comparison_price_and_total_amount(self):
        """Сравнение цены в каталоге и суммы в корзине


        """
        if item_price == cart_total_amount:
            scroll_page = self.driver.find_element(By.XPATH, self.INPUT_SEARCH)
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_page)
            element = self.get_element(xpath=self.INPUT_SEARCH)
            element.send_keys('Суммы совпадают')
            time.sleep(15)
        else:
            scroll_page = self.driver.find_element(By.XPATH, self.INPUT_SEARCH)
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_page)
            element = self.get_element(xpath=self.INPUT_SEARCH)
            element.send_keys('Сумма ', item_price, ' не равна ', cart_total_amount)
            time.sleep(15)
