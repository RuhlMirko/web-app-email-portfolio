import smtplib
import ssl
import os


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()

    username = "ruhlmirkojoel@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "mirkaapo.709@gmail.com"
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

