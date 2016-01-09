import unittest

from selenium import webdriver

from test_support import pages


class BlankSignIN(unittest.TestCase):
    """   Test that check impossibility to sign in with empty email and password    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://news360.com/")
        self.driver.implicitly_wait(10)

    def test_blank_signin(self):
        """ Tests normal signin with empty email and password  """
        main_page = pages.MainPage(self.driver)
        main_page.click_signin_link()
        main_page.set_email('')
        main_page.set_password('')
        main_page.click_signin_button()
        text = main_page.return_message_text(*pages.MainPageLocators.EMAIL_PARSING_ERROR)
        self.assertEquals(text, 'This value is required.', 'The messages are different!')


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()