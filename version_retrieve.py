from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.python.org/')

menu = driver.find_element_by_id('downloads').click()

version = ""

main = WebDriverWait(driver, 10).until(ec.presence_of_element_located
                                       ((By.XPATH, "//*[@id='content']/div/section/div[2]/ol")))
articles = main.find_elements_by_tag_name("li")
for article in articles:
    header = article.find_element_by_class_name("release-number")
    version = header.text
    break

print(version)
