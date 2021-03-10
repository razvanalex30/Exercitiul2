from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
import re


class VersionRetrieve:

    @staticmethod
    def string_parse(input_str):
        version_number = re.findall(r'[0-9]+.[0-9]+.[0-9]+', input_str)
        return version_number[0]

    @classmethod
    def navigate(cls):
        driver = webdriver.Chrome('./chromedriver')
        driver.get('https://www.python.org/')
        return driver

    @classmethod
    def find_path(cls):
        driver = cls.navigate()
        menu = driver.find_element_by_xpath(
            "//ul[@class='navigation menu']//li[contains(@class,'tier-1 element-')]/a[text()='Downloads']")
        ac = ActionChains(driver)
        ac.move_to_element(menu).perform()
        driver.find_element_by_xpath(
            "//ul[@class='navigation menu']//ul[@class='subnav menu']//li[contains(@class,'tier-2 element-')]//a["
            "text()='All releases']").click()
        return driver

    @classmethod
    def retrieve_version(cls):
        driver = cls.find_path()
        last_version = "The most recent Python version is: "
        all_releases = WebDriverWait(driver, 10).until(ec.presence_of_element_located
                                                       ((By.XPATH, "//*[@id='content']/div/section/div[2]/ol")))
        version = all_releases.find_elements_by_tag_name("li")[0]
        header = version.find_element_by_class_name("release-number")
        version_number = cls.string_parse(header.text)
        last_version += version_number
        return last_version


print(VersionRetrieve.retrieve_version())
