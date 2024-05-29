from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SideBar(Page):
    GO_TO_MENU=(By.CSS_SELECTOR, "a[href*='/main-menu']")

    def go_to_menu(self):
        self.click(*self.GO_TO_MENU)