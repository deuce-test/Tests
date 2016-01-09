import unittest

from selenium import webdriver

from test_support.pages import MainPage, MainPageLocators


class LogInLink(unittest.TestCase):
    """A sample test class to show how 'Log in' link works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("https://news360.com/")


    def test_login_link(self):
        """        Tests 'Log in' link        """
        main_page = MainPage(self.driver)
        main_page.click_signin_link()
        main_page.click_signup_link()
        main_page.click_login_link()
        assert main_page.is_element_present(*MainPageLocators.SIGNIN_EMAIL_FIELD)
        assert main_page.is_element_present(*MainPageLocators.SIGNIN_PASSWORD_FIELD)
        assert main_page.is_element_present(*MainPageLocators.SIGNIN_BUTTON)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()