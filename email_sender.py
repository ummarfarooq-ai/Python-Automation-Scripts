import smtplib

def send_email(sender, password, receiver, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender, password)
    server.sendmail(sender, receiver, message)

    print("Email sent successfully.")

    server.quit()


if __name__ == "__main__":
    sender = "your_email@gmail.com"
    password = "your_password"
    receiver = "receiver_email@gmail.com"
    message = "Hello, this is a test email from Python."

    send_email(sender, password, receiver, message)
