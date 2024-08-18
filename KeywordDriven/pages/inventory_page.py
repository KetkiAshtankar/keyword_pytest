from selenium.webdriver.common.by import By
from utils.waits import wait_for_element, wait_for_element_clickable

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")
        self.cart_button = (By.CLASS_NAME, 'shopping_cart_link')

    def add_item_to_cart(self, item_name):
        item_selector = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        wait_for_element_clickable(self.driver, *item_selector).click()

    def go_to_cart(self):
        wait_for_element_clickable(self.driver, *self.cart_button).click()
