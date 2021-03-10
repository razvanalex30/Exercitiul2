from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class VersionRetrieve:

    @classmethod
    def retrieve_version(cls):
        driver = webdriver.Chrome('./chromedriver')
        driver.get('https://www.python.org/')
        driver.find_element_by_id('downloads').click()
        lastversion = ""
        main = WebDriverWait(driver, 10).until(ec.presence_of_element_located
                                               ((By.XPATH, "//*[@id='content']/div/section/div[2]/ol")))
        versions = main.find_elements_by_tag_name("li")
        for version in versions:
            header = version.find_element_by_class_name("release-number")
            lastversion = header.text
            break
        return lastversion


print(VersionRetrieve.retrieve_version())
