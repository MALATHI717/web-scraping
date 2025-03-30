import requests
from bs4 import BeautifulSoup
import json

# Fetch the web page
url = "https://kissflow.com/"
response = requests.get(url)
data = response.text

# Parse the HTML content
soup = BeautifulSoup(data, 'html.parser')

# Find the footer section
footer = soup.find('footer', class_='brand-footer')
# print(footer)

# Extract footer content
footer_data = {}
if footer:
    # Extract text content
    footer_text = footer.get_text(separator="\n", strip=True)
    # print(footer_text)
    # Extract links
    links = footer.find_all('a')
    footer_links = {link.text.strip(): link['href'] for link in links if link.get('href') and link.text}
    
    # Store data in JSON format
    footer_data = {
        # "footer_text": footer_text,
        "footer_links": footer_links
    }
else:
    footer_data = {"error": "Footer not found"}

# Convert to JSON format and save to a file
with open("footer_data.json", "w", encoding="utf-8") as json_file:
    json.dump(footer_data, json_file, indent=4, ensure_ascii=False)

print("JSON file 'footer_data.json' has been created successfully!")