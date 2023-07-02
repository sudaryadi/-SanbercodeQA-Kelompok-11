from selenium import webdriver
from pageObject.signUp import SignUp

class UserSignUp:
    base_url = "https://www.demoblaze.com"
    username = "Sudaryadi"
    password = "Admin123"

    def test_signUp(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.reg = SignUp(self)
        self.reg.click_button_signUp()
        self.reg.input_username(self.username)
        self.reg.input_password(self.password)
        self.reg.click_submit_signUp()
