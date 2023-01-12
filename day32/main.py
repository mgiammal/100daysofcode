import random
import smtplib

import pandas
import datetime as dt

PLACEHOLDER = "[NAME]"
my_email = "REPLACE_ME"


def load_birthdays_dict():
    birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")
    return birthdays


def update_letter_text(letter, name):
    """
    Opens letter file and updates the Name placeholder and returns the text
    :param letter:
    :param name:
    :return:
    """
    with open(f"letter_templates/{letter}", "r") as ltr:
        letter_template = ltr.read()
    letter_template = letter_template.replace("[NAME]", name)
    return letter_template


def send_email(letter_text, to_email):
    pw = "REPLACE_ME"
    gmail_smtp = "smtp.gmail.com"

    with smtplib.SMTP(gmail_smtp) as new_connection:
        new_connection.starttls()
        new_connection.login(user=my_email, password=pw)
        new_connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg=f"Subject:Happy Birthday!\n\n{letter_text}")


birthdays_dict = load_birthdays_dict()

now = dt.datetime.now()
month = now.month
day = now.day

for birthday in birthdays_dict:
    if birthday.get("month") == month and birthday.get("day") == day:
        letter_file = f"letter_{random.randint(1,3)}.txt"
        letter_txt = update_letter_text(letter_file, birthday.get("name"))
        send_email(letter_txt, birthday.get("email"))
