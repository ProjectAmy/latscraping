import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.bhinneka.com/jual?cari=iphone")

print(r)

soup = BeautifulSoup(r.content, 'html.parser')

produk = soup.find_all("h6", class_="o_wsale_products_item_title mb-2")
nama_produk = []

for item in produk:
    nama = item.find('a').get_text()
    nama_produk.append(nama)
    print(nama)

