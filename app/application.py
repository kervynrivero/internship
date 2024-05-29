from pages.base_page import Page
from pages.sign_in_page import SigninPage
from pages.sidebar import SideBar
from pages.main_menu_page import MainMenuPage
class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_menu_page = MainMenuPage(driver)
        self.side_bar = SideBar(driver)
        self.sign_in_page = SigninPage(driver)