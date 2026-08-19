import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random

WEEK_DAY = 2


def get_quote():
    with open("quotes.txt") as file:
        lines = file.readlines()
        rdm_index = random.randint(0, len(lines))
        return lines[rdm_index]


now = dt.datetime.now()
current_week_day = now.weekday()
print("day of the week:", current_week_day)

if current_week_day == WEEK_DAY:
    load_dotenv()
    my_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("APP_PASSWORD")
    recipient = os.getenv("RECIPIENT_EMAIL")
    smtp_server = os.getenv("SMTP_SERVER")
    quote = get_quote()
    print("quote:", quote)

    with smtplib.SMTP(smtp_server) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=f"Subject:Happy Wendnesday\n\n{quote}",
        )
