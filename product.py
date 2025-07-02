import requests
from bs4 import BeautifulSoup
import pandas as pd

# Flipkart search URL for mobiles
url = "https://www.flipkart.com/search?q=mobiles"

# Add headers to look like a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Send request and parse HTML
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Find data
names = soup.find_all("div", class_="_4rR01T")
prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
ratings = soup.find_all("div", class_="_3LWZlK")

# Store in list
products = []
for i in range(min(len(names), len(prices), len(ratings))):
    products.append({
        "Name": names[i].text,
        "Price": prices[i].text,
        "Rating": ratings[i].text
    })

# Save to CSV
df = pd.DataFrame(products)
df.to_csv("products.csv", index=False)

print("✅ Product data saved to 'products.csv'")

