import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random
import pandas as pd
from email.mime.text import MIMEText

##################### Extra Hard Starting Project ######################

load_dotenv()
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("APP_PASSWORD")
smtp_server = os.getenv("SMTP_SERVER")

now = dt.datetime.now()
current_day = now.day
current_month = now.month

def get_birthdays():
    data_frame = pd.read_csv("birthdays.csv")
    rows = data_frame[data_frame.day == current_day]
    rows = rows[rows.month == current_month]
    print(rows)
    return rows


def get_letter_name():
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    rdm_idx = random.randint(0, 2)
    return letters[rdm_idx]


def get_letter_template(letter_name):
    with open(f"letter_templates/{letter_name}", encoding="utf-8") as file:
        template = file.read()
        return template

def send_email(recipient_email, message):
       msg = MIMEText(message, "plain", "utf-8")
       msg["Subject"] = "Happy Birthday!"
       msg["From"] = sender_email
       msg["To"] = recipient_email

       with smtplib.SMTP(smtp_server) as connection:
            connection.starttls()
            connection.login(sender_email, password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=recipient_email,
                msg=msg.as_string(),
            )

rows = get_birthdays()
letter_name = get_letter_name()
letter_template = get_letter_template(letter_name)

if len(rows) > 0:
    for index, row in rows.iterrows():
        name = row["name"]
        email = row["email"]
        message = letter_template.replace("[NAME]", name)
        print(message)
        send_email(email, message)
