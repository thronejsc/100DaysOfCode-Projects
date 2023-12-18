##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
from random import choice
import pandas

now = dt.datetime.now()

letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

my_email = "tmacgravy21@gmail.com"
password = "qcvu ulxx qgds stqc"

birthday_data = pandas.read_csv("birthdays.csv")

birthday_list = birthday_data.to_dict(orient="records")

for i in birthday_list:
    if i['month'] == now.month and i['day'] == now.day:
        random_template = choice(letter_templates)

        with open(f"./letter_templates/{random_template}") as letter:
            data = letter.read()
            greeting = data.replace("[NAME]", i['name'])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=i['email'], msg=f"Subject:Birthday Greeting\n\n{greeting}")
