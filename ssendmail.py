Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import smtplib
>>> server=smtplib.SMTP('smtp.gmail.com',587)
>>> server.starttls()
(220, b'2.0.0 Ready to start TLS')
>>> server.login('send_from','password')
(235, b'2.7.0 Accepted')
>>> server.sendmail('send_from','send_to','hi ajay')
{}
>>> 
