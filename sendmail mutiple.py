# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 

# Authentication

 
# list of email_id to send the mail
li = ["send_to 1", "send_to 2","send_to 3"]
 
for i in range(len(li)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("send_from", "password")
    message = "Message_you_need_to_send"
    s.sendmail("send_from", li[i], message)
    s.quit()
