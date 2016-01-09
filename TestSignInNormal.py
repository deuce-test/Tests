import unittest

from selenium import webdriver

from test_support import pages


class SignInNormal(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://news360.com/")
        self.driver.implicitly_wait(10)

    def test_normal_signin(self):
        """
        Tests normal signin
        """
        main_page = pages.MainPage(self.driver)
        main_page.click_signin_link()
        main_page.set_email('asd@asd.il')
        main_page.set_password('111112')
        main_page.click_signin_button()
        opened_page = pages.DashboardPage(self.driver)
        assert opened_page.is_page_opened(), "Dashboard page is not opened"



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()