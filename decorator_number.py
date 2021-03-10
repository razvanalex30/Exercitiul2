from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org")
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("decorator")
search_bar.send_keys(Keys.RETURN)
results = WebDriverWait(driver, 10).until(ec.presence_of_element_located
                                               ((By.XPATH, "//*[@id='content']/div/section/form/ul")))
