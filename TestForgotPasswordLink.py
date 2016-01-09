import unittest

from selenium import webdriver

from test_support.pages import MainPage, MainPageLocators


class ForgotPasswordLink(unittest.TestCase):
    """ A sample test class to show how 'Forgot your password' link UI works """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("https://news360.com/")


    def test_forgot_pass_link(self):
        """ Test ForgotPasswordLink checks 'Forgot your password' link UI """
        main_page = MainPage(self.driver)
        main_page.click_signin_link()
        main_page.click_forgot_pass_link()
        assert main_page.is_element_present(*MainPageLocators.RESET_PASSWORD_BUTTON)
        main_page.set_credential('asd@asd.il', *MainPageLocators.RESET_EMAIL_FIELD)
        main_page.click_reset_button()
        main_page.wait_for_element(30, MainPageLocators.SUCCESSFULL_RESET_MESSAGE)
        text = main_page.return_message_value(*MainPageLocators.SUCCESSFULL_RESET_MESSAGE)
        self.assertEquals(text, 'We emailed you a link to reset your password', 'The messages are different!')  # Message parametrization will be required for localized site

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()