from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title': [1,2], 'price': [3,4], 'link': [1, 2]}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        t = soup.find("h2")
        title = t.get_text()
        p = soup.find("span", class_="a-price-whole")
        price = p.get_text()
        # We are searching for a's inside the h2 tag
        l = t.find("a") 
        link = "https://amazon.in/" + l['href']
        #We can check is it working fine by printing as well print(title, price)
        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link) 
    except Exception as e:
        print(e)
        continue

df = pd.DataFrame(d) 
df.to_csv("data.csv", index=False)




