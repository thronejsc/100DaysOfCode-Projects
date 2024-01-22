

FROM_EMAIL = "tmacgravy21@gmail.com"
PASSWORD = "qcvu ulxx qgds stqc"

header = {
    "Accept-Language": "en-GB,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"
}






import requests
from bs4 import BeautifulSoup
import smtplib


product_url = "https://www.amazon.com/dp/B08C4X9VR5/?th=1"


response = requests.get(url=product_url, headers=header)

webpage = response.text

soup = BeautifulSoup(webpage,"lxml")

item_price = float(soup.find(name="span", class_="a-offscreen").getText().strip("$"))
item_original_price = float(soup.find(name="span", class_="a-price a-text-price").find(class_="a-offscreen").getText().strip("$"))
item_product = soup.find(name="span", id="productTitle").getText().strip(" ")


message = f"Subject:AMAZON PRICE ALERT\n\n{item_product} is now ${item_price}\n{product_url}"

# IM GONNA DECREASE THE ITEM_PRICE FOR TESTING

if item_price-10 < 70:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=FROM_EMAIL,
            password=PASSWORD
        )
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=FROM_EMAIL,
            msg=message
        )