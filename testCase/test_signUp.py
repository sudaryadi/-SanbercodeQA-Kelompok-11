from selenium import webdriver
from pageObject.signUp import SignUp


class TestUserSignUp:
    base_url = "https://www.demoblaze.com"
    username = "Sudaryadi"
    password = "Admin123"

    def test_signup(self):
        self.driver = webdriver.Chrome(executable_path="./webdriver/chromedriver.exe")
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        # Menggunakan import class SignUp dari pageObject
        self.reg = SignUp(self)
        self.reg.click_button_signup()
        self.reg.input_username(self.username)
        self.reg.input_password(self.password)
        self.reg.click_submit_signup()
