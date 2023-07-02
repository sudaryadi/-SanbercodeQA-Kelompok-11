from selenium import webdriver
from pageObject.signUp import SignUp

class SignUp:
    base_url = "https://www.demoblaze.com"
    username = "Sudaryadi"
    password = "Admin123"

    def test_signUp(self):
        