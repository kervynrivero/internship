from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SideBar(Page):
    GO_TO_MENU=(By.CSS_SELECTOR, "a[href*='/main-menu']")
    GO_TO_MENU_mobile=(By.CSS_SELECTOR, "a.assistant-button.w-inline-block")

    def go_to_menu(self):

        if self.driver.is_mobile:
            self.click(*self.GO_TO_MENU_mobile)
        else:
            self.click(*self.GO_TO_MENU)