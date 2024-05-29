from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SigninPage(Page):

    USER_EMAIL=(By.ID, 'email-2')
    USER_PASSWORD=(By.ID, 'field')
    SIGN_IN_BUTTON=(By.CSS_SELECTOR,"a.login-button.w-button")
    def open_sign_in_page(self):
        self.open('https://soft.reelly.io/sign-in')

    def login_user(self, email, password):
        self.input_text(email, *self.USER_EMAIL)
        self.input_text(password, *self.USER_PASSWORD)
        self.click(*self.SIGN_IN_BUTTON)
        sleep(6)
