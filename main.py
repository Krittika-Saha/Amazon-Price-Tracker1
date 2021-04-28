import smtplib
from bs4 import BeautifulSoup
import requests

with open('file.txt', 'r') as file:
  email = file.readlines()[0].strip('\n')
  password = open('file.txt', 'r').readlines()[1]

product_link = _YOUR_LINK_HERE_
html_doc = requests.get(product_link, headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
})
soup = BeautifulSoup(html_doc.content, "html.parser")
product_title = (soup.find('span', id='productTitle', class_='a-size-large product-title-word-break').text).strip()
price = float((soup.find("span", id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString").text).split("₹")[1])
max_price = _YOUR_PRICE_HERE_
if price <= max_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs='krittika.saha.dev@gmail.com', msg=f"""Subject:Buy {product_title} at your preferred price!\n\n
{product_title} is available at {max_price} or lower!
Buy now!
Product Link: {product_link}""")


#TODO: 1. Use BeautifulSoup to Scrape the Product Price ✅
#TODO: 2. Email Alert When Price Below Preset Value ✅
