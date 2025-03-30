import requests
from bs4 import BeautifulSoup
import json

# Step 1: Fetch the Webpage Content
url = "http://www.sangathamizh.com/18keezh-kanakku/18keezh-kanakku-iniyavainatpathu-இனியவைநாற்பது.html"
response = requests.get(url)
response.encoding = 'utf-8'  
# print(response)
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup)

centersection_div = soup.find('div', id='centerSection')
# print(len(centersection_div))

data_list = []
number = 1
for item in centersection_div.find_all("div",id="centerContent"):
    if item.find("div",id="sub-header"):
        title = item.find("div",id="p1").text.strip()
        description = item.find("p").text
        data_list.append({"number":number,"title": title, "description": description})
        number+=1
        
with open("hello.json", "w", encoding="utf-8") as json_file:
    json.dump(data_list, json_file, indent=4, ensure_ascii=False)