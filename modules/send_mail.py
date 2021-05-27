import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_mail(to, mail_content):
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
        try:
            content = MIMEMultipart()
            content["subject"] = "Top 5 CPU usage"
            content["from"] = "gn01809864@gmail.com"
            content["to"] = to
            content.attach(MIMEText(mail_content))
            smtp.ehlo()
            smtp.starttls()
            smtp.login("gn01809864@gmail.com", os.environ.get('GMAIL_TOKEN'))
            smtp.send_message(content)
            print(f"Send email to {to} successfully")
        except Exception as e:
            print("Error message: ", e)