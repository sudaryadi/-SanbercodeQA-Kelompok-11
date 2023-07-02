from selenium.webdriver.common.by import By


class SignUp:
    btn_signUp_linkText = "Sign up"
    txt_username_id = "sign-username"
    txt_password_id = "sign-password"
    btn_signUp_xpath = '//*[@id="signInModal"]/div/div/div[3]/button[2]'

    def __init__(self, driver) -> None:
        self.driver = driver()
    
    def open_url(self, base_url):
        self.driver.find_element(By.LINK_TEXT, self.btn_signUp_linkText).click()
    
    def input_username(self, username):
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(username)
    
    def input_password(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)
    
    def click_signUp(self):
        self.driver.find_element(By.XPATH, self.btn_signUp_xpath).click()
