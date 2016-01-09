import unittest

from selenium import webdriver

from test_support.pages import MainPageLocators, MainPage


class SignUpShort(unittest.TestCase):
    """ Test that check that user can't sign up with not long enough password """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://news360.com/")
        self.driver.implicitly_wait(10)

    def test_short_password_signup(self):
        """ Test SignUpShort checks that user can't sign up with not long enough password """
        main_page = MainPage(self.driver)
        main_page.click_signin_link()
        main_page.click_signup_link()
        main_page.set_credential('asdcx@vb.com', *MainPageLocators.SIGNUP_EMAIL_FIELD)
        main_page.set_credential('555', *MainPageLocators.SIGNUP_PASSWORD_FIELD)
        main_page.set_credential('555', *MainPageLocators.SIGNUP_PASSWORD_CONFIRM)
        main_page.click_signup_button()
        text = main_page.return_message_value(*MainPageLocators.SHORT_PASS_MESSAGE)
        self.assertEquals(text, "This value is too short. It should have 6 characters or more.", 'The messages are different!')


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()