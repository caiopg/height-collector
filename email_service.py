from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email = "ENTER GMAIL USED TO SEND"
    from_pass = "ENTER GMAIL PASSWORD"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>. Average height of %s people is <strong>%s</strong>.<br>Thanks!" % (height, count, average_height)

    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_pass)
    gmail.send_message(msg)
