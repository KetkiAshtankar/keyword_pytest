from selenium.webdriver.common.by import By
from utils.waits import wait_for_element_clickable

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, 'first-name')
        self.last_name_input = (By.ID, 'last-name')
        self.postal_code_input = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.finish_button = (By.ID, 'finish')

    def enter_checkout_information(self, first_name, last_name, postal_code):
        wait_for_element_clickable(self.driver, *self.first_name_input).send_keys(first_name)
        wait_for_element_clickable(self.driver, *self.last_name_input).send_keys(last_name)
        wait_for_element_clickable(self.driver, *self.postal_code_input).send_keys(postal_code)

    def click_continue(self):
        wait_for_element_clickable(self.driver, *self.continue_button).click()

    def click_finish(self):
        wait_for_element_clickable(self.driver, *self.finish_button).click()
