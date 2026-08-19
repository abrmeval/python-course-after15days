# Sending emails with smtplib

```python
import smtplib
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()
my_email = os.getenv("SENDER_EMAIL")
password = os.getenv("APP_PASSWORD")
recipient = os.getenv("RECIPIENT_EMAIL")
smpt_server = os.getenv("SMTP_SERVER")

# Sending an email with smtplib
with smtplib.SMTP(smpt_server) as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient,
        msg="Subject:Hello\n\n This is the body of the message",
    )

# Handling datetime
# Returns the current date in an specific format
now = dt.datetime.now()
print(now)
print(now.year)  # => Returns the current year only
print(now.date())  # => Returns the current Date part only
print(now.hour)  # => Returns the current hour only
print(now.time())  # => Returns the time part of the DateTime
print(
    now.weekday()
)  # => returns the current day of the week as an integer (number of the day of the current week)

date = dt.datetime(year=1995, month=12, day=15) # Create a custom DateTime
print(date)
```
