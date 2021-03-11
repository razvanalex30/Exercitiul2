from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options


class CheckExamples:

    @classmethod
    def navigate(cls):
        """
        Method used to navigate to Python's Official Website
        :return: driver, necessary for completing other tasks on the webpage
        """
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome('./chromedriver', options=chrome_options)
        driver.get('https://www.python.org/')
        return driver

    @classmethod
    def search(cls):
        """
        Method used to search in the search bar of the site and press Enter to find results
        """
        driver = cls.navigate()
        search_bar = driver.find_element_by_name("q")
        search_bar.clear()
        search_bar.send_keys("decorator")
        search_bar.send_keys(Keys.RETURN)
        return driver

    @classmethod
    def get_first_result(cls):
        """
        Method used to click on the first result from the search list
        """
        driver = cls.search()
        results_view = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//ul[@class='list-recent-events "
                                                      "menu']")))
        first_result = results_view.find_element_by_xpath(
            "//a[text()='PEP 318 -- Decorators for Functions and Methods']")
        ac = ActionChains(driver)
        ac.move_to_element(first_result).click(first_result).perform()
        return driver

    @classmethod
    def open_content_examples(cls):
        """
        Method used to click on the Examples submenu from the Contents menu
        """
        driver = cls.get_first_result()
        content_view = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//article[@class='text']")))
        content_view_example = content_view.find_element_by_xpath("//ul[@class='simple']//a[text()='Examples']")
        ac2 = ActionChains(driver)
        ac2.move_to_element(content_view_example).click(content_view_example).perform()
        return driver

    @classmethod
    def verify_example_count(cls):
        """
        Verify the number of examples presented in the Examples paragraph of the page
        :return: True if the number of examples in the Example sections is 5, False otherwise
        """
        driver = cls.open_content_examples()
        examples_view = driver.find_element_by_xpath("//div[@id='examples']//ol[@class='arabic']")
        examples_list = examples_view.find_elements_by_tag_name("li")
        if len(examples_list) == 5:
            print("Yes, there are {} examples".format(str(len(examples_list))))

        else:
            print("No, there are {} examples".format(str(len(examples_list))))
        return driver

    @classmethod
    def driver_quit(cls):
        driver = cls.verify_example_count()
        driver.quit()


CheckExamples.driver_quit()
