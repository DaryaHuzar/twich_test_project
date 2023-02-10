from pages.base_page import BasePage
from pages.locators import home_page_locators as apl


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url)

    def navigate(self):
        self.driver.get("https://www.twitch.tv/")

    def get_title(self):
        return self.driver.title

    def click_first_recommended_channel(self):
        self.find_element(apl.first_recommended_channel).click()
