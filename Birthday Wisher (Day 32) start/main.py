import smtplib
import random

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1997 , month=6,day = 11)
print(date_of_birth)

with open("quotes.txt",mode="r") as data:
    data_file = data.readlines()
    data_file = [i.strip("\n") for i in data_file]

def quote_sender(day):
    if day == 4:
        quote = random.choice(data_file)
        my_email = YOUR EMAIL
        password = YOUR PASSWORD
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # securing connection
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=EMAIL TO SEND,
                                msg=f"Subject:Quote of the week\n\n {quote}")

quote_sender(day_of_week)