import unittest

from selenium import webdriver

from test_support.pages import MainPageLocators, MainPage


class ResetPassEqual(unittest.TestCase):
    """ A sample test class to show that equal passwords are required during password resetting """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("https://news360.com/#~ffb82714-3715-4f9e-8c45-db6aadc439e9") # This link is to be replaced when corresponding link obtaining mechanism is to be created.


    def test_reset_password_equal(self):
        """ Test ResetPassEqual checks that passwords provided by user should be equal """
        main_page = MainPage(self.driver)
        main_page.set_credential('555555', *MainPageLocators.NEW_PASSWORD)
        main_page.set_credential('666666', *MainPageLocators.CONFIRM_PASSWORD)
        main_page.click_confirm_button()
        text = main_page.return_message_value(*MainPageLocators.NON_EQUAL_MESSAGE)
        self.assertEquals(text, 'This value should be the same.', 'The messages are different!')  # Message parametrization will be required for localized site

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()