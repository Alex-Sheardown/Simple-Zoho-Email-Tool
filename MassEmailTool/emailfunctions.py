import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from tkinter import*
import csv
import os
import pandas as pd
import row


#sends an email through an SMTP Server via ZohoMail.
#TODO: error reporting for invalid inputs
#TODO: prevent email from getting sent to spam
def SendEmail(subject ,message, from_addr, to_addr, password):

    #body of email
    msg = MIMEMultipart()
    msg.attach(MIMEText(message))

    #subject of email
    msg['Subject'] = subject

    #sender of the email
    msg['From'] = from_addr

    #receiver of the email
    msg['To'] = to_addr


    try:
    #open server, and send an email

        server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
        server.login(from_addr, password)
        #send message

        server.send_message(msg)
        print('email sent successfully!')
        #close server

        server.quit()
    except smtplib.SMTPException as e:
        print(f"SMTP Exception: {e}")
    except Exception as e:
        print(f"Error: {e}")



#sends emails to multiple addresses using a subject, message, sender's email, API password, and a CSV File.
#reads in emails list from a CSV using Pandas, and builds a message from the 'emailbody.txt' file.
#Fields: Subject: Email's subject as a string. 
#emailMessage: txt file containing an email message to append into email
#from_addr: the sender's email address from Zoho Mail.
#password: The user's API key from Zoho Mail.
#myCsv: CSV file containing information to be read in by Pandas.

def bulkEmail(subject, emailMessage, from_addr, password, myCSV):
    
    #try to read in txt file containing message
    
    try:
        with open(emailMessage,'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print('file not found! sad face.')
    except Exception as e:
        print("an error has occurred: " + {e})
    
    #try to read in CSV file containing names and email addresses
    
    try:
        mySheet = pd.read_csv(myCSV)
    except FileNotFoundError:
        print("file not found!")
    except Exception as e:
        print("An error has occurred" + {e})

    cwd = os.getcwd()
    
    with open(myCSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Read as dictionary
        #header = next(reader)
        for row in reader:
            file = open("emailbody.txt")
            template=file.read()
            file.close()

            # Replace placeholders with corresponding values
            message = template
            email_to_send = ""
            for key in row:  # Iterate over headers
                if key == "email":
                    email_to_send = row[key]
                message = message.replace(f"[{key}]", row[key])
            print(message)
            SendEmail(subject, message, from_addr, email_to_send , password)
    



"""
#appends a greeting using full name and message into an email.
#utilize itertuples to traverse both columns for emails and names  
    for x, y in mySheet.itertuples(index=False):
        messageToSend = "Dear " + y + "," + "\n \n" + content

        SendEmail(subject,messageToSend,from_addr,x,password)
    
    
"""