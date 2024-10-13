Amazon Web Scraping Project
This project scrapes product data from Amazon using Selenium, BeautifulSoup, and Pandas. The scraped data is collected in HTML format and can be further processed into a CSV file for easier analysis.

Project Overview
The script extracts product information from Amazon based on user-provided queries and pagination settings (i.e., how many pages of results to scrape). It saves the HTML data of the scraped products in a folder named data. Optionally, BeautifulSoup and Pandas can be used to parse this HTML and store the structured data in a CSV file.

Features
Scrapes product details such as titles, prices, and links from Amazon search results.
Saves the raw HTML data of each page into a separate file.
Converts HTML into a CSV file for easier processing and analysis.

Prerequisites
Python3 must be installed on your system.
Google Chrome and the ChromeDriver should be installed for Selenium to work.
Setup Instructions
Clone the repository and navigate into the project directory.

Set up a virtual environment:

bash
Copy code
python -m venv .venv
source .venv/bin/activate   # For Linux/Mac
.venv\Scripts\activate      # For Windows
Install the necessary packages:

bash
Copy code
pip install -r requirements.txt
Create a folder named data in the project root directory where the scraped HTML files will be saved:

bash
Copy code
mkdir data
Running the Web Scraper
Inside the virtual environment, create a Python file named project.py.

The script takes in the user's query and the number of pages to scrape from Amazon.

Run the script with the following command:

bash
Copy code
python project.py
The scraped HTML files will be saved in the data folder.

Converting HTML to CSV
Once the scraping process is complete, you can use BeautifulSoup and Pandas to extract the desired product details from the HTML files and save them in a CSV format.

To do so, modify the project.py file to parse the HTML files and store the data into a CSV file using

Setting the environment for you
<img width="1552" alt="Screenshot 2024-10-13 at 6 56 06 PM" src="https://github.com/user-attachments/assets/2513d725-0d51-4b5e-bdc6-5c8e2fefa0e7">


Here are the final results for you
CSV:
<img width="1552" alt="Screenshot 2024-10-13 at 6 55 18 PM" src="https://github.com/user-attachments/assets/d468244c-b057-4d29-aab2-dd960280f609">
In Excel:
<img width="1552" alt="Screenshot 2024-10-13 at 6 55 48 PM" src="https://github.com/user-attachments/assets/d7015f6c-3199-4a6b-bbcc-0d2c415de0db">
