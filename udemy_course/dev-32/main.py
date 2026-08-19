import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("SENDER_EMAIL")
password = os.getenv("APP_PASSWORD")
recipient = os.getenv("RECIPIENT_EMAIL")
smpt_server = os.getenv("SMTP_SERVER")

with smtplib.SMTP(smpt_server) as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient,
        msg="Subject:Hello\n\n This is the body of the message",
    )
