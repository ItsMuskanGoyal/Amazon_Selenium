from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
for i in range(1, 10):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=3HM8DGNWT44HR&qid=1728817264&sprefix=laptop%2Caps%2C210&ref=sr_pg_2")

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} elements found")
    for elem in elems:
        print(elem.text) 
        print("\n\n\n")
    # print(elem.get_attribute("outerHTML"))
    # print(elem.text)


    time.sleep(5)
    driver.close()