import smtplib

my_email = "REPLACE_ME"
to_email = "REPLACE_ME"
pw = "REPLACE_ME"
gmail_smtp = "smtp.gmail.com"

with smtplib.SMTP(gmail_smtp) as new_connection:
    new_connection.starttls()
    new_connection.login(user=my_email, password=pw)
    new_connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg="Subject:Hello\n\nEmail body")
