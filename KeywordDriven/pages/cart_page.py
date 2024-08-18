from selenium.webdriver.common.by import By
from utils.waits import wait_for_element_clickable

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, 'checkout')

    def click_checkout(self):
        wait_for_element_clickable(self.driver, *self.checkout_button).click()
