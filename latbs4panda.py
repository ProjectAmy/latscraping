import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

r = requests.get("https://www.bhinneka.com/jual?cari=iphone")

print(r)

soup = BeautifulSoup(r.content, 'html.parser')

produk = soup.find_all("div", class_="o_wsale_product_information position-relative d-flex flex-column flex-grow-1 flex-shrink-1")

nama_produk = []
harga_produk = []

for item in produk:
    nama = item.find('a').get_text()
    harga = item.find('span', class_="oe_currency_value").get_text().replace(".", "")
    nama_produk.append(nama)
    harga_produk.append(harga)

produk_dict = {
    'nama' : nama_produk,
    'harga' : harga_produk
}

df = pd.DataFrame(produk_dict, columns=['nama', 'harga'])
df.sort_values('harga', ascending=True)
print(df)

df.to_csv('bhinneka.csv', sep=',')
