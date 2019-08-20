import smtplib
from email.mime.text import MIMEText


def send_email(email, age, average_age, count):
    from_email = "age.collector@gmail.com"
    from_password = "Agecollector2019"
    to_email = email

    subject = "Age data"
    message = "Sizin yaşınız: <strong>%s</strong>. <br>Cəmi yaşların ədədi ortası: <strong>%s</strong>. <br>Sorğuda iştirak edənlərin sayı: <strong>%s</strong> nəfər. <br>Sorğuda iştirak etdiyiniz üçün təşəkkürlər!" % (
    age, average_age, count)

    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
