import smtplib
import os
from email.mime.text import MIMEText

def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = os.getenv("TO_EMAIL")

    with smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT"))) as s:
        s.starttls()
        s.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        s.send_message(msg)