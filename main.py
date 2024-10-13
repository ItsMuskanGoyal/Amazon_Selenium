from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon_muskan")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
#to get some time to see the result
time.sleep(5)
driver.close()