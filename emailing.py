#-*- coding:utf-8-*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys,os,traceback,time,re


sender = 'ifnameravnomain@gmail.com'
passw = 'ifnameravnomain1811'
emails = 'emails_checked.txt'

#open test.txt
f = open(emails, 'r')

def send_mail(): 

    #email =
    for receiver in f.readlines():

        receiver_with_no_nl = re.sub('\n', '', receiver) #receiver seems to have been added \n 

        try:
            time.sleep(10)
            msg = MIMEMultipart()
            msg['Subject'] = 'Resume: эколог (СПб)'
            msg['To'] = receiver_with_no_nl 
            body = '''
            Здравствуйте. Прошу рассмотреть мою кандидатуру. Прилагаю резюме. 

            +79501103887, kornilovoy@gmail.com

            Automatically sent by: Python 3.6.7
            '''

            msg.attach(MIMEText(body, 'plain')) 

            filename = '/home/o/python/hh/resume_KornilovOY.pdf'
            attachment = open(filename, 'rb')  
            p = MIMEBase('application', 'octet-stream') 
            p.set_payload((attachment).read()) 
            encoders.encode_base64(p) 
        
            p.add_header('Content-Disposition', 'attachment; filename=%s' % filename) 
            msg.attach(p) 
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            s.starttls()  
            s.login(sender, passw) 
            
            s.sendmail(sender, receiver_with_no_nl, msg.as_string())

            print('Email sent to', receiver_with_no_nl)
            time.sleep(1)

        except Exception:
            print(traceback.format_exception(*sys.exc_info())[1])
            pass

    s.quit() 

send_mail()

