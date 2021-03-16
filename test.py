# from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from primary_page import PrimaryPage
from downloads_page import DownloadPage
from result_page import ResultPage
from decorator_page import DecoratorPage
import unittest


class TestPage(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome('./chromedriver', options=chrome_options)
        self.driver.get('https://www.python.org/')

    def test_downloads(self):
        driver = self.driver
        primary_page = PrimaryPage(driver)
        primary_page.navigate_menu_submenu("Downloads", "All releases")
        downloads_page = DownloadPage(driver)
        downloads_page.retrieve_version()

    def test_decorators(self):
        driver = self.driver
        primary_page = PrimaryPage(driver)
        primary_page.search("decorator")
        result_page = ResultPage(driver)
        result_page.get_first_result()
        decorator_page = DecoratorPage(driver)
        decorator_page.verify_example_count()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
