from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.amazon.in/")

print(driver.title)

search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("OnePlus 8T")
search.send_keys(Keys.RETURN)

time.sleep(10)
driver.quit()
