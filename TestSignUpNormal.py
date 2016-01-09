import unittest
from selenium import webdriver
from test_support.pages import MainPageLocators, MainPage, DashboardLocators


class SignUpNormal(unittest.TestCase):
    """   Test that check that user can sign up with correct login and password    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://news360.com/")
        self.driver.implicitly_wait(10)

    def test_cancel_signin(self):
        """ Tests normal sign up """
        main_page = MainPage(self.driver)
        main_page.click_signin_link()
        main_page.click_signup_link()
        email = main_page.get_random_email()
        main_page.set_credential(email, *MainPageLocators.SIGNUP_EMAIL_FIELD)
        main_page.set_credential('555555', *MainPageLocators.SIGNUP_PASSWORD_FIELD)
        main_page.set_credential('555555', *MainPageLocators.SIGNUP_PASSWORD_CONFIRM)
        main_page.click_signup_button()
        main_page.wait_for_element(30, DashboardLocators.GREETING_TEXT)
        text = main_page.return_message_value(*DashboardLocators.GREETING_TEXT)
        self.assertEquals(text, "To begin, select a few topics you're interested in", 'The messages are different!')  # Completely optional check


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()