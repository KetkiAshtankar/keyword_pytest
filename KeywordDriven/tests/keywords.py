from pages.login_page import LoginPage
# from pages.inventory_page import
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium import webdriver


class KeywordDriven:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)

    def open_browser(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.login_page.login(username,password)

    def add_item_to_cart(self, item_name):
        self.inventory_page.add_item_to_cart(item_name)

    def go_to_cart(self):
        self.inventory_page.go_to_cart()

    def checkout(self, first_name, last_name, postal_code):
        self.cart_page.click_checkout()
        self.checkout_page.enter_checkout_information(first_name, last_name, postal_code)
        self.checkout_page.click_continue()

    def finish_checkout(self):
        self.checkout_page.click_finish()
