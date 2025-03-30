import requests
from bs4 import BeautifulSoup
import json

url = "http://www.sangathamizh.com/18keezh-kanakku/18keezh-kanakku-ainthinaiaimpathu-%E0%AE%90%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%A3%E0%AF%88%E0%AE%90%E0%AE%AE%E0%AF%8D%E0%AE%AA%E0%AE%A4%E0%AF%81.html"
response = requests.get(url)
response.encoding = 'utf-8'  
soup = BeautifulSoup(response.text, 'html.parser')
centersection_div = soup.find('div', id='centerSection')

list = []
number = 1
for item in centersection_div.find_all("div",id="centerContent"):
    if item.find("div",id="sub-header"):
        title = item.find("div",id="p1").text.strip()
        description = item.find("p").text
        list.append({"number":number,"title": title, "description": description})
        number+=1
        
with open("new.json", "w", encoding="utf-8") as json_file:
    json.dump(list, json_file, indent=4, ensure_ascii=False)