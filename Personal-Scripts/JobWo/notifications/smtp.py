import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_email(html):
    sender = os.getenv("JOBWO_EMAIL")
    password = os.getenv("JOBWO_EMAIL_PASSWORD")

    receiver = sender

    message = EmailMessage()
    message["Subject"] = "JobWo - New Jobs"
    message["From"] = sender
    message["To"] = receiver

    message.set_content("Your email client does not support HTML.")
    message.add_alternative(html, subtype="html")

    with smtplib.SMTP("smtp.h-da.de", 587) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(message)
