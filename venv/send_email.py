import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

try:
    print('Sending email.....')

#getting the html file and reading it
    html = Template(Path('emailBody.html').read_text())

#setting up email infos
    email = EmailMessage()
    email['from'] = ''
    email['to'] = ''
    email['subject'] = ''
#setting email content and variables for html content
    email.set_content(html.substitute({'name' : 'Marley'}), 'html') #this is a sample data

#information to login in the sender email account and setting up stmplib infos
    my_email = ''
    my_email_password=''
    host = 'smtp.gmail.com' #this is a sample data
    port = 587 #this is a sample data

#login in the sender email account and send the email
    with smtplib.SMTP(host, port) as smtp :
        smtp.ehlo()
        smtp.starttls()
        smtp.login(my_email,my_email_password)
        smtp.send_message(email)

#handling possibles errors
except (smtplib.SMTPAuthenticationError, smtplib.SMTPSenderRefused, smtplib.SMTPConnectError, smtplib.SMTPServerDisconnected) as error:
    print(f'something went wrong, \n this is what happened : {error}')

else:
#print if everythig goes fine
    print("The email has been successfuly sent")