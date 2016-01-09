from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SIGNIN_LINK = (By.XPATH, "//a[@class='fancybox login-signin ng-binding']")  # This link will be found first since one from pop-up is below in page code.
    SIGNUP_LINK = (By.XPATH, "//form[@class='signin ng-pristine ng-valid']//a[@class='signup ng-binding']")
    LOGIN_LINK = (By.XPATH, "//form[@class='signup ng-pristine ng-valid']//a[@class='login ng-binding']")
    FORGOT_PASSWORD_LINK = (By.CLASS_NAME, 'forgotpass ng-binding')
    #"//form[@class='signin ng-pristine ng-valid']/a[@class='forgotpass ng-binding'"
    SIGNIN_EMAIL_FIELD = (By.XPATH, "//input[@id='signinemail']")
    SIGNIN_PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")  # I found it more convenient than finding by name
    SIGNUP_EMAIL_FIELD = (By.ID, "signupemail")
    SIGNUP_PASSWORD_FIELD = (By.XPATH, "//form[@class='signup ng-pristine ng-valid']//input[@id='password']")
    SIGNUP_PASSWORD_CONFIRM = (By.XPATH, "//form[@class='signup ng-pristine ng-valid']//input[@class='confirmpassword textbox']")
    SIGNIN_BUTTON = (By.XPATH, "//button[@class='green-button ladda-button signin-button ng-binding']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@class='green-button ladda-button signup-button ng-binding']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@class='confirm-button green-button ladda-button ng-binding']")
    CANCEL_BUTTON = (By.XPATH, "//form[@class='signin ng-pristine ng-valid']/*/button[@class='cancel-button green-button ladda-button ng-binding']")
    EMAIL_PARSING_ERROR = (By.XPATH, "//li[@class='required']")
    PASSWORD_CONFIRM_ERROR = (By.XPATH, "//input[@class='confirmpassword textbox parsley-validated parsley-error']/following-sibling::*/li[@class='required']")
    INVALID_CREDENTIALS_MESSAGE = (By.XPATH, "//div[@class='error-message message ng-binding']")
    INVALID_LOGIN_MESSAGE = (By.XPATH, "//div[@class='bHSignIn']/div[@class='error-message message ng-binding']")
    NON_EQUAL_MESSAGE = (By.CLASS_NAME, "equalto")
    SHORT_PASS_MESSAGE =(By.CLASS_NAME, "minlength")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@class='forgotpass ng-binding']")
    RESET_PASSWORD_BUTTON = (By.XPATH, "//button[@class='green-button ladda-button reset-button ng-binding']")
    RESET_EMAIL_FIELD = (By.ID, "resetemail")
    SUCCESSFULL_RESET_MESSAGE = (By.XPATH, "//div[@class='message success-message']/div[@class='t']")
    NEW_PASSWORD = (By.ID, "resetpassword")
    CONFIRM_PASSWORD = (By.XPATH, "//input[@class='confirmpassword textbox']")


    #  "//div[@class='message success-message']/div[@class='t']"


    GO_BUTTON = (By.ID, 'submit')

class DashboardLocators(object):
    """A class for dashboard page locators. Locators viewed by logged in user is collected here"""
    EXPLORE_BUTTON = (By.XPATH, "//a[@class='explore explorehint ng-binding']")
    GREETING_TEXT = (By.XPATH, "//div[@class='explore intro ng-scope']/h3[@class='ng-binding']")

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass