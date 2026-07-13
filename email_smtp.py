from email.message import EmailMessage
import smtplib
import ssl
from datetime import datetime
import time

EMAIL = "itzz.hardik@gmail.com"
PASSWORD = "oiro tdsc rqvn figk"

recipients = [
    "iamnishitshinde@gmail.com",
    "person2@gmail.com",
    "person3@gmail.com"
]

msg = EmailMessage()

msg["Subject"] = "Love letter"
msg["From"] = EMAIL

# Show all recipients in the To field
msg["To"] = ", ".join(recipients)

msg.set_content("Hello everyone,\n\nPlease find the attached report.")

# Attach a file
with open("Tiger.jpg", "rb") as img:
    msg.add_attachment(
        img.read(),
        maintype="image",
        subtype="jpg",
        filename="Tiger.jpg"
    )

context = ssl.create_default_context()

#scheduling


with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(EMAIL, PASSWORD)
    smtp.send_message(msg)

print("Email sent!")