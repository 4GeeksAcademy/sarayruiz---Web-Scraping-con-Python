import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

resource_url = 'https://www.lalibelulademarta.com/tienda?Categor%C3%ADa=-Packs'
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
headers = {"User-Agent": agent}
response = requests.get(resource_url, headers=headers)
response.status_code

soup = BeautifulSoup(response.content)
soup

products = soup.find_all('div', class_='EiRAO9')

list_products = []

for product in products:
    product_name_elements = product.find_all('p', class_='sIzEbfk oYnQqx0---typography-11-runningText oYnQqx0---priority-7-primary syHtuvM FzO_a9')
    product_price_elements = product.find_all('span', class_='cfpn1d')
    product_name = product_name_elements[-1].text

    if product_price_elements:
        price_text = product_price_elements[-1].text
    else:
        price_text = 'N/A'

    list_products.append({'Producto': product_name,
                          'Precio': price_text})
list_products

df = pd.DataFrame(list_products)
y = df['Producto']
x = df['Precio']

plt.bar(x, y, color='darkmagenta')
plt.show()

plt.plot(x, y, color='red', linestyle='--')
plt.title('Articulos y Precios')
plt.xlabel('Precios')
plt.ylabel('Articulos')
plt.show()
