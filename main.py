from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.python.org/')
# print(driver.title)
menu = driver.find_element_by_id('downloads').click()


try:
    main = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/section/div[1]/ol/li[1]")))
    print(type(main.text))
except:
    driver.quit()



