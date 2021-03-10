from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains


class VersionRetrieve:

    @classmethod
    def navigate(cls):
        driver = webdriver.Chrome('./chromedriver')
        driver.get('https://www.python.org/')
        return driver

    @classmethod
    def find_path(cls):
        driver = cls.navigate()
        menu = driver.find_element_by_xpath("//ul[@class='navigation menu']//li[contains(@class,'tier-1 element-')]/a[text("
                                     ")='Downloads']")
        last_version = "The most recent Python version is:"
        ac = ActionChains(driver)
        ac.move_to_element(menu).perform()
        driver.find_element_by_xpath("//ul[@class='navigation menu']//ul[@class='subnav menu']//li[contains(@class,'tier-2 element-')]//a[text()='All releases']").click()

        all_releases = WebDriverWait(driver, 10).until(ec.presence_of_element_located
                                               ((By.XPATH, "//*[@id='content']/div/section/div[2]/ol")))
        versions = all_releases.find_elements_by_tag_name("li")
        for version in versions:
            header = version.find_element_by_class_name("release-number")
            last_version += header.text[6::]
            break
        return last_version

# VersionRetrieve.navigate()
print(VersionRetrieve.find_path())
