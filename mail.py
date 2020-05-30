import smtplib
from email.message import EmailMessage
Email_Addr = <sender_email>
Email_pass = <password>
msg = EmailMessage()
msg['Subject'] = "Model Trained Successfully"
msg['From'] = Email_Addr
msg['To'] = <receiver_email>
msg.set_content("Model trained successfully and accuracy achived is more than 95.0%")
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Email_Addr, Email_pass)
    smtp.send_message(msg)