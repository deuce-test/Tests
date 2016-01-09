import unittest

from selenium import webdriver

from test_support import pages


class BlankEmailSignIN(unittest.TestCase):
    """   Test that check impossibility to sign in with empty email    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://news360.com/")
        self.driver.implicitly_wait(10)

    def test_blank_signin(self):
        """ Tests normal signin with empty email  """
        main_page = pages.MainPage(self.driver)
        main_page.click_signin_link()
        main_page.set_email('')
        main_page.set_password('111112')
        main_page.click_signin_button()
        text = main_page.return_message_text(*pages.MainPageLocators.EMAIL_PARSING_ERROR)
        self.assertEquals(text, 'This value is required.', 'The messages are different!')  # Message parametrization will be required for localized site


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()