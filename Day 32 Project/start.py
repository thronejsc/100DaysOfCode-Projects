import smtplib
import datetime as dt
from random import choice

now = dt.datetime.now()

my_email = "tmacgravy21@gmail.com"
password = "qcvu ulxx qgds stqc"

to_email = "tmacgravy21@myyahoo.com"

if now.weekday() == 4:
    with open("quotes.txt") as quotes:
        quote = quotes.readlines()
        random_quote = choice(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Motivation\n\n{random_quote}")









