import smtplib, ssl
import os


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "zigouris.konstantinos@gmail.com"
    password = os.getenv("news_api_email_pass")

    recipient = "zigouris.konstantinos@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, recipient, message)
