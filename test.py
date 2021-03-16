# from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from primary_page import PrimaryPage
from downloads_page import DownloadPage
from result_page import ResultPage
from decorator_page import DecoratorPage
import unittest
# from functools import wraps


# def decorator_driver_quit(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         driver = TestPage.setUp()
#         func(*args,**kwargs)
#         print("Process executed!")
#         driver.close()
#         print("Driver was stopped successfully!")
#
#     return wrapper

class TestPage(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome('./chromedriver', options=chrome_options)
        self.driver.maximize_window()
        self.driver.get('https://www.python.org/')

    def test_downloads(self):
        try:
            print("Test_downloads in progress...")
            driver = self.driver
            primary_page = PrimaryPage(driver)
            primary_page.navigate_menu_submenu("Downloads", "All releases")
            downloads_page = DownloadPage(driver)
            downloads_page.retrieve_version()
            print("Test executed successfully!")
        except Exception as e:
            print(e, "Test_downloads error")
            pass

    def test_decorators(self):
        try:
            print("Test_decorators in progres...")
            driver = self.driver
            primary_page = PrimaryPage(driver)
            primary_page.search("decorator")
            result_page = ResultPage(driver)
            result_page.get_first_result("PEP 318 -- Decorators for Functions and Methods")
            decorator_page = DecoratorPage(driver)
            decorator_page.verify_example_count()
            print("Test executed successfully!")
        except Exception as e:
            print(e, "Test_decorators error")
            pass

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
