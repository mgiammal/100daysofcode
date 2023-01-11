import random
import smtplib
import datetime as dt


def load_quotes():
    with open("../birthdaywisherstart/quotes.txt", "r") as quotes:
        quote_list = [quote.replace("\n", "") for quote in quotes]
    return quote_list


def send_email(email_body):
    my_email = "REPLACE_ME"
    to_email = "REPLACE_ME"
    pw = "REPLACE_ME"
    gmail_smtp = "smtp.gmail.com"

    with smtplib.SMTP(gmail_smtp) as new_connection:
        new_connection.starttls()
        new_connection.login(user=my_email, password=pw)
        new_connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg=f"Subject:Monday Motivation\n\n{email_body}")


q_list = load_quotes()

if dt.datetime.now().weekday() == 0:
    send_email(random.choice(q_list))
