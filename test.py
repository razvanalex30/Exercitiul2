from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from primary_page import PrimaryPage


class TestPage:

    @classmethod
    def navigate(cls):
        """
        Method used to start a Chrome Websession and navigate to Python's Official Website
        :return: driver, necessary for completing other tasks on the webpage
        """
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome('./chromedriver', options=chrome_options)
        cls.driver.get('https://www.python.org/')


    def test(self):
        driver = self.driver
        primary_page = PrimaryPage(driver)
        # primary_page.navigate_menu_submenu("Downloads","All releases")
        primary_page.search("decorator")


TestPage().navigate()
t = TestPage()
t.test()