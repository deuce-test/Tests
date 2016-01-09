import unittest

from selenium import webdriver

from test_support.pages import MainPageLocators, MainPage


class CancelSignIN(unittest.TestCase):
    """   Test that check that Cancel button works at sign in    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://news360.com/")
        self.driver.implicitly_wait(10)

    def test_cancel_signin(self):
        """ Tests Cancel button  """
        main_page = MainPage(self.driver)
        main_page.click_signin_link()
        main_page.set_email('asd@asd.il')
        main_page.set_password('555555')
        main_page.click_cancel_button()
        text = main_page.return_message_text(*MainPageLocators.SIGNIN_LINK)
        self.assertEquals(text, 'Sign in with email', 'The messages are different!')


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()