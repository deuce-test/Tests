import unittest

from selenium import webdriver

from test_support.pages import MainPageLocators, MainPage


class SignUpEmpty(unittest.TestCase):
    """   Test that checks that user can sign up with empty password    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://news360.com/")
        self.driver.implicitly_wait(10)

    def test_empty_signup(self):
        """ Test SignUpEmpty checks empty password processing during sign up """
        main_page = MainPage(self.driver)
        main_page.click_signin_link()
        main_page.click_signup_link()
        email = main_page.get_random_email()
        main_page.set_credential(email, *MainPageLocators.SIGNUP_EMAIL_FIELD)
        main_page.set_credential('', *MainPageLocators.SIGNUP_PASSWORD_FIELD)
        main_page.set_credential('', *MainPageLocators.SIGNUP_PASSWORD_CONFIRM)
        main_page.click_signup_button()
        text = main_page.return_message_value(*MainPageLocators.EMAIL_PARSING_ERROR)
        self.assertEquals(text, "This value is required.", 'The messages are different!')
        text = main_page.return_message_value(*MainPageLocators.PASSWORD_CONFIRM_ERROR)
        self.assertEquals(text, "This value is required.", 'The messages are different!')


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()