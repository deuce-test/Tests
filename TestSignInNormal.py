import unittest

from selenium import webdriver

from test_support import pages


class SignInNormal(unittest.TestCase):
    """ A sample test class to check sign in with valid credentials """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://news360.com/")
        self.driver.implicitly_wait(10)

    def test_normal_signin(self):
        """ Test SignInNormal checks normal sign in with valid credentials """
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