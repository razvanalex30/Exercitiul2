from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import datetime
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
        # last_version = "The most recent Python version is: "
        all_releases = self.driver.find_element_by_xpath("//*[@id='content']/div/section/div[2]/ol")
        versions = all_releases.find_elements_by_tag_name("li")
        release_list = []
        for version in versions:
            version_dict = {'release_version': None, 'release_date': None}
            header = version.find_element_by_class_name("release-number")
            header_2 = version.find_element_by_class_name("release-date")
            # version_number = self.string_parse(header.text)
            version_dict['release_version'] = header.text

            # last_version += version_number
            print(header.text)

    def retrieve_table_version(self):
        self.find_path()
        last_python_version = self.driver.find_element_by_xpath("//ol[@class='list-row-container menu']//li//span["
                                                                "text()='3.9']")
        last_active_version = last_python_version.text
        print(last_active_version)


version_last = VersionRetrieve()
version_last.retrieve_version()
