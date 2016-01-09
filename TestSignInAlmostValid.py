import unittest

from selenium import webdriver

from test_support import pages


class SignInAlmostValid(unittest.TestCase):
    """ A sample test class to test inability to use someone else's password to sign in """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://news360.com/")
        self.driver.implicitly_wait(10)

    def test_almost_normal_signin(self):
        """ Test SignInAlmostValid checks that user can't use someone else's password during sign in """
        main_page = pages.MainPage(self.driver)
        main_page.click_signin_link()
        main_page.set_email('asd@asd.il')
        main_page.set_password('444444')
        main_page.click_signin_button()
        text = main_page.return_message_value(*pages.MainPageLocators.INVALID_CREDENTIALS_MESSAGE)
        self.assertEquals(text, 'Invalid login or password', 'The messages are different!')  # Message parametrization will be required for localized site



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()