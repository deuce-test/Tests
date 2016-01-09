import unittest

from selenium import webdriver

from test_support.pages import MainPageLocators, MainPage


class SignUpEqual(unittest.TestCase):
    """   Test that check that user can't sign up with unconfirmed password    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://news360.com/")
        self.driver.implicitly_wait(10)

    def test_password_signup_equal(self):
        """ Test SignUpEqual checks password confirmation mechanism during sign up """
        main_page = MainPage(self.driver)
        main_page.click_signin_link()
        main_page.click_signup_link()
        main_page.set_credential('asdcx@vb.com', *MainPageLocators.SIGNUP_EMAIL_FIELD)
        main_page.set_credential('555555', *MainPageLocators.SIGNUP_PASSWORD_FIELD)
        main_page.set_credential('5555555', *MainPageLocators.SIGNUP_PASSWORD_CONFIRM)
        main_page.click_signup_button()
        text = main_page.return_message_value(*MainPageLocators.NON_EQUAL_MESSAGE)
        self.assertEquals(text, "This value should be the same.", 'The messages are different!')


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()