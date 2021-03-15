# from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from primary_page import PrimaryPage
from downloads_page import DownloadPage
from result_page import ResultPage
from decorator_page import DecoratorPage


class TestPage:

    @classmethod
    def navigate(cls):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome('./chromedriver', options=chrome_options)
        cls.driver.get('https://www.python.org/')

    def test(self):
        driver = self.driver
        primary_page = PrimaryPage(driver)
        # primary_page.navigate_menu_submenu("Downloads","All releases")
        primary_page.search("decorator")
        # downloads_page = DownloadPage(driver)
        # downloads_page.retrieve_version()
        result_page = ResultPage(driver)
        result_page.get_first_result()
        decorator_page = DecoratorPage(driver)
        decorator_page.verify_example_count()


TestPage().navigate()
t = TestPage()
t.test()
