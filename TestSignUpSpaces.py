import unittest

from selenium import webdriver

from test_support.pages import MainPageLocators, MainPage


class SignUpSpaces(unittest.TestCase):
    """ Test that check that user can't sign up with password containing only spaces """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://news360.com/")
        self.driver.implicitly_wait(10)

    def test_spaces_signup(self):
        """ Test SignUpSpaces checks that password containing only space characters can't be used in sign up """
        main_page = MainPage(self.driver)
        main_page.click_signin_link()
        main_page.click_signup_link()
        email = main_page.get_random_email()
        main_page.set_credential(email, *MainPageLocators.SIGNUP_EMAIL_FIELD)
        main_page.set_credential('      ', *MainPageLocators.SIGNUP_PASSWORD_FIELD)
        main_page.set_credential('      ', *MainPageLocators.SIGNUP_PASSWORD_CONFIRM)
        main_page.click_signup_button()
        main_page.wait_for_element(10, MainPageLocators.INVALID_CREDENTIALS_MESSAGE)
        text = main_page.return_message_value(*MainPageLocators.INVALID_CREDENTIALS_MESSAGE)
        self.assertEquals(text, 'Invalid login or password', 'The messages are different!')  # Message parametrization will be required for localized site


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()