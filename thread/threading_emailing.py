#-*- coding:utf-8-*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys,os,traceback,time,re
from threading import Thread


sender = 'test1raw@gmail.com'
passw = 'testRAW1811'

def send_mail(emails, sleep_index): 

    #open test.txt
    f = open(emails, 'r')

    #email =
    for receiver in f.readlines():

        receiver_with_no_nl = re.sub('\n', '', receiver) #receiver seems to have been added \n 

        try:
            time.sleep(sleep_index)
            msg = MIMEMultipart()
            msg['Subject'] = 'Resume: эколог (СПб)'
            msg['To'] = receiver_with_no_nl 
            body = '''
            Здравствуйте. Прошу рассмотреть мою кандидатуру. Прилагаю резюме. 

            +79501103887, kornilovoy@gmail.com

            Automatically sent by: Python 3.6.7'''
            

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

        except Exception:
            print(traceback.format_exception(*sys.exc_info())[1])
            pass

    s.quit() 


thread1 = Thread(target=send_mail, args=('emails_checked.txt', 2))
thread2 = Thread(target=send_mail, args=('emails_checked2.txt', 5))

thread1.start()
thread2.start()
thread1.join()
thread2.join()