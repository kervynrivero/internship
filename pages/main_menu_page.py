from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class MainMenuPage(Page):
    RUSSIAN_LANGUAGE=(By.CSS_SELECTOR, "a[lang*='ru']")
    ENGLISH_LANGUAGE=(By.CSS_SELECTOR, "a[lang*='en']")
    LANGUAGE_HEADER = (By.CSS_SELECTOR, "div[class='language-in-header _1']")
    RUSSIAN_LANGUAGE_HEADER = (By.CSS_SELECTOR, "div[lang='ru']")
    ENGLISH_LANGUAGE_HEADER = (By.CSS_SELECTOR, "div[lang='en']")
    #mobile locators
    LANGUAGE_HEADER_MOBILE = (By.CSS_SELECTOR, "div.wg-dropdown-1")
    CHANGE_Languague = (By.CSS_SELECTOR,"#w-dropdown-list-0")
    def change_language(self, context, language):

        if self.driver.is_mobile:

            self.click(*self.LANGUAGE_HEADER_MOBILE)
            self.click(*self.CHANGE_Languague)

        else:
            hover_element = self.find_element(*self.LANGUAGE_HEADER)
            ActionChains(context.driver).move_to_element(hover_element).perform()

            if language == 'russian':
                self.wait_until_clickable_click(*self.RUSSIAN_LANGUAGE)
            else:
                self.wait_until_clickable_click(*self.ENGLISH_LANGUAGE)
            sleep(4)

    def verify_language(self, language):
        if language == 'russian':
            self.find_element(*self.RUSSIAN_LANGUAGE_HEADER)
        else:
            self.find_element(*self.ENGLISH_LANGUAGE_HEADER)