import smtplib

smtp_server = "smtp.example.com"
smtp_port = 587
sender_email = "your_email@example.com"
receiver_email = "recipient@example.com"
password = "your_password"

message = """\
Subject: My Email Subject

This is the email body."""

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


#This code demonstrates how to send an email using the smtplib library with a SMTP server.