import unittest

from selenium import webdriver

from test_support import pages


class BlankPassSignIN(unittest.TestCase):
    """   Test that check impossibility to sign in with empty password    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://news360.com/")
        self.driver.implicitly_wait(10)

    def test_blank_signin(self):
        """ Tests normal signin with empty password  """
        main_page = pages.MainPage(self.driver)
        main_page.click_signin_link()
        main_page.set_email('asd@asd.il')
        main_page.set_password('')
        main_page.click_signin_button()
        text = main_page.return_message_value(*pages.MainPageLocators.INVALID_LOGIN_MESSAGE)
        self.assertEquals(text, 'Invalid login or password', 'The messages are different!')  # Message parametrization will be required for localized site


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()