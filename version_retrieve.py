from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import re


class VersionRetrieve:
    """
    Class used to retrieve the last Python Version from Python's official website
    """

    def __init__(self):
        self.driver = None

    @staticmethod
    def string_parse(input_str):
        """
        Method used to retrieve the Python Version
        :param input_str: Python Version string obtained from the site
        :return: Retains only the version number
        """
        version_number = re.findall(r'[0-9]+.[0-9]+.[0-9]+', input_str)
        return version_number[0]

    def navigate(self):
        """
        Method used to start a Chrome Websession and navigate to Python's Official Website
        :return: driver, necessary for completing other tasks on the webpage
        """
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome('./chromedriver', options=chrome_options)
        self.driver.get('https://www.python.org/')

    def find_path(self):
        """
        Method used to find the path to Downloads -> All releases menu
        """
        self.navigate()
        menu = self.driver.find_element_by_xpath(
            "//ul[@class='navigation menu']//li[contains(@class,'tier-1 element-')]/a[text()='Downloads']")
        ac = ActionChains(self.driver)
        ac.move_to_element(menu).perform()
        self.driver.find_element_by_xpath(
            "//ul[@class='navigation menu']//ul[@class='subnav menu']//li[contains(@class,'tier-2 element-')]//a["
            "text()='All releases']").click()

    def retrieve_version(self):
        """
        Method used to retrieve the last python version from the table available in All releases
        """
        self.find_path()
        last_version = "The most recent Python version is: "
        all_releases = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located
                                                            ((By.XPATH, "//*[@id='content']/div/section/div[2]/ol")))
        version = all_releases.find_elements_by_tag_name("li")[0]
        header = version.find_element_by_class_name("release-number")
        version_number = self.string_parse(header.text)
        last_version += version_number
        print(last_version)


version_last = VersionRetrieve()
version_last.retrieve_version()
