import requests
from bs4 import BeautifulSoup
page = requests.get("https://finance.yahoo.com/quote/TSLA/")

soup = BeautifulSoup(page.content, 'html.parser')

prevCloseClass = soup.find(class_="Ta(end) Fw(600) Lh(14px)")

prevPrice = prevCloseClass.find(class_="Trsdu(0.3s)").get_text()

print("TSLA Previous Close Price is $" + prevPrice)

