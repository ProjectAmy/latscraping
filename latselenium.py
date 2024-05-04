# latihan menggunakan selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options # menambah opsi browser
from selenium.webdriver.common.by import By # untuk nantinya mencari elemen

chrome_option = Options()
chrome_option.add_argument('--ignore-certificate-errors') # kalo ada SSL error maka dilewati

browser = webdriver.Chrome(options=chrome_option)
browser.get('https://www.rei.com/')

# element = browser.find_element(By.XPATH, '//*[@id="headerWrapper"]/section/section/section/div[2]/form/div/input')
element = browser.find_element(By.CLASS_NAME, 'search__input')
element.send_keys("jacket for men")