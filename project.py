from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
    
# Create a directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

driver = webdriver.Chrome()
query = "laptop"
file = 0
for i in range(1, 10):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=3HM8DGNWT44HR&qid=1728817264&sprefix=laptop%2Caps%2C210&ref=sr_pg_2")

    # Find all elements by class name
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} elements found on page {i}")
    
    # Iterate over elements and write their outerHTML to files
    for elem in elems:
        d = elem.get_attribute("outerHTML")  # Get the HTML content
        if d:  # Ensure that the element's outerHTML is not None
            with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
                f.write(d)
            file += 1

    time.sleep(5)

driver.close()
