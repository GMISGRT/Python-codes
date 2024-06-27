import smtplib #pip install smtplib
import ssl #pip install ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = input("Enter your address:")  # Enter your address
receiver_email = input("Enter the receiver address:")  # Enter receiver address
# Gmail App DJANGO Password "wlcvfhwuqunavhtp"
password = input("Type your password and press enter: ")
message = """\Subject: Hi there
This message is sent from LingarajTechhub.
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    
#https://realpython.com/python-send-email/
#https://temp-mail.org/ temp mail generator
#https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/
#https://zetcode.com/python/smtplib/
#https://myaccount.google.com/apppasswords (To Create Localhost Mail Access)


#python send mail with attachment