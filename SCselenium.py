from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# latihan study case 1

browser = webdriver.Chrome()
browser.get('https://books.toscrape.com/catalogue/category/books/mystery_3/index.html')

produk = browser.find_elements(By.CLASS_NAME, 'product_pod')

daftar_buku = []

for item in produk:
    judul = item.find_element(By.CSS_SELECTOR, "h3 > a").get_attribute("title")
    harga = item.find_element(By.CLASS_NAME, 'price_color').text

    daftar_produk = {
        'judul' : judul,
        'harga' : harga
    }
    daftar_buku.append(daftar_produk)

df = pd.DataFrame(daftar_buku)
print(df)

df.to_csv('bookscrao.csv')