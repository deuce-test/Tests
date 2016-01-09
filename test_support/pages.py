import random
import string
from locators import MainPageLocators, DashboardLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, *locator):
        element = self.driver.find_element(*locator)
        element.click()

    def set_text(self, text, *locator):
        element = self.driver.find_element(*locator)
        element.click()
        element.send_keys(text)

    def wait_for_element(self, delay, locator):
        WebDriverWait(self.driver, delay).until(EC.visibility_of_element_located(locator))

    def is_element_present(self, *locator):
        element = self.driver.find_element(*locator)
        return element

    def return_message_text(self, *locator):
        element = self.driver.find_element(*locator)
        return element.text

    def return_message_value(self, *locator):
        element = self.driver.find_element(*locator)
        return element.get_attribute('innerHTML')

    def get_random_email(self):
        email_account = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        domain = 'xcv.com'
        email = email_account + '@' + domain
        return email


class MainPage(BasePage):
    """Home page action methods come here."""

    def click_signin_link(self):
        super(MainPage, self).click_element(*MainPageLocators.SIGNIN_LINK)

    def click_signup_link(self):
        super(MainPage, self).click_element(*MainPageLocators.SIGNUP_LINK)

    def set_email(self, text):
        super(MainPage, self).set_text(text, *MainPageLocators.SIGNIN_EMAIL_FIELD)

    def set_password(self, text):
        super(MainPage, self).set_text(text, *MainPageLocators.SIGNIN_PASSWORD_FIELD)

    def set_credential(self, text, *locator):
        super(MainPage, self).set_text(text, *locator)

    def click_signin_button(self):
        super(MainPage, self).click_element(*MainPageLocators.SIGNIN_BUTTON)

    def click_confirm_button(self):
        super(MainPage, self).click_element(*MainPageLocators.CONFIRM_BUTTON)

    def click_signup_button(self):
        super(MainPage, self).click_element(*MainPageLocators.SIGNUP_BUTTON)

    def click_cancel_button(self):
        super(MainPage, self).click_element(*MainPageLocators.CANCEL_BUTTON)

    def click_login_link(self):
        super(MainPage, self).click_element(*MainPageLocators.LOGIN_LINK)

    def click_forgot_pass_link(self):
        super(MainPage, self).click_element(*MainPageLocators.FORGOT_PASSWORD_LINK)

    def click_reset_button(self, *locator):
        super(MainPage, self).click_element(*MainPageLocators.RESET_PASSWORD_BUTTON)



class DashboardPage(BasePage):
    """Methods specific for page opened to logged in user are provided here"""

    def is_page_opened(self):
        element = self.driver.find_elements(*DashboardLocators.EXPLORE_BUTTON)
        return element
