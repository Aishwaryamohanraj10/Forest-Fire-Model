import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

def send_email_alert(message):

    msg = MIMEText(message)
    msg['Subject'] = "🔥 Forest Fire Alert"
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_RECEIVER

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
        server.quit()

        print("📧 Email alert sent!")

    except Exception as e:
        print("Email failed:", e)