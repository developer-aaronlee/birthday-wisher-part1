import smtplib
import datetime as dt
import random

my_email = "pythonautomationapp@gmail.com"
password = "dxabiogqxlleamrw"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="automation.python@yahoo.com",
#                         msg="Subject: Hello\n\nThis is email body.")

# now = dt.datetime.now()
# year = now.year
# month = now.month
# weekday = now.weekday()
# print(weekday)
#
# date_of_birth = dt.datetime(year=2000, month=1, day=1)
# print(date_of_birth)


now = dt.datetime.now()
date_of_week = now.weekday()

if date_of_week == 4:
    with open("quotes.txt") as file:
        quotes = file.readlines()

    selected_quote = quotes[random.randint(1, 102)]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="automation.python@yahoo.com",
                            msg=f"Subject: test\n\n{selected_quote}")