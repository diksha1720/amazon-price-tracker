import requests
from bs4 import BeautifulSoup
import lxml

import smtplib


product_url = 'https://www.amazon.com/Smartwatch-Monitor-Tracker-Fitness-Detection/dp/B096BK7W5M/ref=sr_1_3?crid=UDJNHWCS3QM5&keywords=samsung%2Bsmart%2Bwatch%2Bfor%2Bwomen&qid=1641365701&sprefix=samsung%2Bsmart%2Bwatch%2Bfor%2Bwomen%2Caps%2C331&sr=8-3&th=1'


def create_mail(product, price):
    msg =f"Subject: Price Dropped!!\n\n\n Your {product}'s price dropped down to {price}$.\n\nHead over to the link to buy now\n\n\n{product_url} "
    send_mail(msg)


def send_mail(msg):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()

        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="mailtest809@yahoo.com",
                            msg=msg)


my_email = "your email"
password = "your password"


headers = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Defined",
    "Accept-Language": "en-US,en;q=0.9,la;q=0.8,hi;q=0.7",
    }
response = requests.get(url=product_url, headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, "lxml")
price = float(soup.find(name='span', class_='apexPriceToPay').getText().split('$')[1])
product = soup.select_one('#productTitle').getText().split('4')[0].strip()

if price < 210.0:
    create_mail(product, price)

