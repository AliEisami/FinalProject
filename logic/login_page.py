from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage


class LoginPage(BaseAppPage):
    LOGIN_EMAIL_INPUT = '//input[@type="email"]'
    LOGIN_PASSWORD_INPUT = '//input[@type="password"]'
    CONTINUE_BUTTON = '//button[@id="login-submit"]'
    LOGIN_ERROR = '//section[@data-testid="form-error"]'

    def __init__(self, driver):
        """
            Initializes an instance of LoginPage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)

    def fill_login_email_input(self, email):
        """ Fills the login email input with the given email. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.LOGIN_EMAIL_INPUT)))
        try:
            login_email_input = self._driver.find_element(By.XPATH, self.LOGIN_EMAIL_INPUT)
            login_email_input.send_keys(email)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def fill_login_password_input(self, password):
        """ Fills the login password input with the given password. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.LOGIN_PASSWORD_INPUT)))
        try:
            login_password_input = self._driver.find_element(By.XPATH, self.LOGIN_PASSWORD_INPUT)
            login_password_input.send_keys(password)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def continue_button_click(self):
        """ Clicks on the continue button. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.CONTINUE_BUTTON)))
        try:
            continue_button = self._driver.find_element(By.XPATH, self.CONTINUE_BUTTON)
            continue_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def login_flow(self, email, password):
        """
            Executes the login flow with the given email and password.
            Args:
                email: Email to use for login.
                password: Password to use for login.
        """
        self.fill_login_email_input(email)
        self.continue_button_click()
        self.fill_login_password_input(password)
        self.continue_button_click()
