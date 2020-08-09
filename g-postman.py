"""
MIT License

Copyright (c) 2020 Batuhan Gonenc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
from datetime import datetime
from pygame import mixer as mx

#defining-UI-variables
now = datetime.now()
today =now.strftime("%D")
now_hour =now.strftime("%H")
now_minute=now.strftime("%M")
#---------------------------

print("""~
G-Postman
~
Postman's calendar --> {}
Postman's clock --> {} : {}
--------------
G-Postman warns:
-only if it is a special mail add anything like this "@example.com".
-in other situations,i only need the address until "@"(except @).
~
Enjoy.

#Options
---------
0-Gmail to Protonmail
1-Gmail to Gmail
2-Gmail to Yahoo
3-Gmail to Yaani
4-Gmail to Hotmail
5-Gmail to Special Mail
-------------
for exit 'q'.
-------------
**********************""".format(today,now_hour,now_minute))

#music-section
mx.init()
mx.music.load("relaxation.mp3")
mx.music.play(999)

#where-all-the-things-go-on
while True:
    s1 = input("**********\nchoose one(for options 'o'.):")
    
    if s1 =="q":
        print("Good Bye.")
        sys.exit()
        
    elif s1 =='o':
        print("----------\n1-gmail to gmail\n2-gmail to special mail\n3-special mail to gmail\n4-special mail to special mail\nfor exit 'q'.\n----------")
        
    elif s1 == "0":
        sendermail = input("*****\nsender e-mail(gmail):")

        sendermail += "@gmail.com"

        senderpassword=input("*****\npassword:")
        subject = input("subject:")

        receiver = input("*****\nreceiver e-mail(gmail):")
        receiver += "@gmail.com"

        switcher1 = input("*****\nWhich one do you prefer?\nto leave a little message by hand(m)\nenter the path that shows the document.(p)")

        if switcher1 == "m":
            content = input("*****\nenter your message:")

        elif switcher1 == "p":
            pathto = input("*****\nenter the path(it must be in .txt format.):")
            try:
                file = open(pathto,"r")
                content = file.read()
                file.close()
            except:
                print("----------\n#something went wrong#\n#try to check out the file#\n#it can be missed or moved.#")
                continue
        else:
            print("#unvalid process code#")
            break

        message = MIMEMultipart("alternative")

        message["Subject"] = subject
        message["From"] = sendermail
        message["To"] = receiver

        message_content = MIMEText(content,"plain")
        message.attach(message_content)

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context)as server:
                server.login(sendermail,senderpassword)
                server.sendmail(
                sendermail,receiver,message.as_string()
                )
                file = open("mailimg.txt","r")
                img = file.read()
                file.close()
                print("-----><-----\n{}-----><-----".format(img))
                print("*****************\nemail sent successfull.\nHave a nice day!")
        except:
            print("****************\nsomething went wrong.")
            
            
    elif s1 == "1":
        sendermail = input("*****\nsender e-mail(gmail):")

        sendermail += "@gmail.com"

        senderpassword=input("*****\npassword:")
        subject = input("subject:")

        receiver = input("*****\nreceiver e-mail(gmail):")
        receiver += "@gmail.com"

        switcher1 = input("*****\nWhich one do you prefer?\nto leave a little message by hand(m)\nenter the path that shows the document.(p)")

        if switcher1 == "m":
            content = input("*****\nenter your message:")

        elif switcher1 == "p":
            pathto = input("*****\nenter the path(it must be in .txt format.):")
            try:
                file = open(pathto,"r")
                content = file.read()
                file.close()
            except:
                print("----------\n#something went wrong#\n#try to check out the file#\n#it can be missed or moved.#")
                continue
        else:
            print("#unvalid process code#")
            break

        message = MIMEMultipart("alternative")

        message["Subject"] = subject
        message["From"] = sendermail
        message["To"] = receiver

        message_content = MIMEText(content,"plain")
        message.attach(message_content)

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context)as server:
                server.login(sendermail,senderpassword)
                server.sendmail(
                sendermail,receiver,message.as_string()
                )
                file = open("mailimg.txt","r")
                img = file.read()
                file.close()
                print("-----><-----\n{}-----><-----".format(img))
                print("*****************\nemail sent successfull.\nHave a nice day!")
        except:
            print("****************\nsomething went wrong.")
    
    
    elif s1 =="2":
        sendermail = input("*****\nsender e-mail(gmail):")

        sendermail += "@gmail.com"

        senderpassword=input("*****\npassword:")
        subject = input("subject:")

        receiver = input("*****\nreceiver e-mail(yahoo):")
        receiver += "@yahoo.com"

        switcher1 = input("*****\nWhich one do you prefer?\nto leave a little message by hand(m)\nenter the path that shows the document.(p)")

        if switcher1 == "m":
            content = input("*****\nenter your message:")

        elif switcher1 == "p":
            pathto = input("*****\nenter the path(it must be in .txt format.):")
            try:
                file = open(pathto,"r")
                content = file.read()
                file.close()
            except:
                print("-----------\n#something went wrong#\n#try to check out the file#\n#it can be missed or moved.#")
                continue
        else:
            print("#unvalid process code#")
            break

        message = MIMEMultipart("alternative")

        message["Subject"] = subject
        message["From"] = sendermail
        message["To"] = receiver

        message_content = MIMEText(content,"plain")
        message.attach(message_content)

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context)as server:
                server.login(sendermail,senderpassword)
                server.sendmail(
                sendermail,receiver,message.as_string()
                )
                file = open("mailimg.txt","r")
                img = file.read()
                file.close()
                print("-----><-----\n{}-----><-----".format(img))
                print("*****************\nemail sent successfull.\nHave a nice day!")
        except:
            print("****************\nsomething went wrong.")
    
    
    elif s1 =="3":
        sendermail = input("*****\nsender e-mail(gmail):")
        sendermail +="@gmail.com"

        senderpassword=input("*****\npassword:")
        subject = input("subject:")

        receiver = input("*****\nreceiver e-mail(yaani):")
        receiver += "@yaani.com"

        switcher1 = input("*****\nWhich one do you prefer?\nto leave a little message by hand(m)\nenter the path that shows the document.(p)")

        if switcher1 == "m":
            content = input("*****\nenter your message:")

        elif switcher1 == "p":
            pathto = input("*****\nenter the path(it must be in .txt format.):")
            try:
                file = open(pathto,"r")
                content = file.read()
                file.close()
            except:
                print("----------\n#something went wrong#\n#try to check out the file#\n#it can be missed or moved.#")
                continue
        else:
            print("#unvalid process code#")
            break

        message = MIMEMultipart("alternative")

        message["Subject"] = subject
        message["From"] = sendermail
        message["To"] = receiver

        message_content = MIMEText(content,"plain")
        message.attach(message_content)

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context)as server:
                server.login(sendermail,senderpassword)
                server.sendmail(
                sendermail,receiver,message.as_string()
                )
                file = open("mailimg.txt","r")
                img = file.read()
                file.close()
                print("-----><-----\n{}-----><-----".format(img))
                print("*****************\nemail sent successfull.\nHave a nice day!")
        except:
            print("****************\nsomething went wrong.")
    
    
    elif s1 =="4":
        sendermail = input("*****\nsender e-mail(gmail):")
        sendermail += "@gmail.com"
        
        senderpassword=input("*****\npassword:")
        subject = input("subject:")

        receiver = input("*****\nreceiver e-mail(hotmail):")
        receiver+="@hotmail.com"

        switcher1 = input("*****\nWhich one do you prefer?\nto leave a little message by hand(m)\nenter the path that shows the document.(p)")

        if switcher1 == "m":
            content = input("*****\nenter your message:")

        elif switcher1 == "p":
            pathto = input("*****\nenter the path(it must be in .txt format.):")
            try:
                file = open(pathto,"r")
                content = file.read()
                file.close()
            except:
                print("----------\n#something went wrong#\n#try to check out the file#\n#it can be missed or moved.#")
                continue
        else:
            print("unvalid process code..")
            break

        message = MIMEMultipart("alternative")

        message["Subject"] = subject
        message["From"] = sendermail
        message["To"] = receiver

        message_content = MIMEText(content,"plain")
        message.attach(message_content)

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context)as server:
                server.login(sendermail,senderpassword)
                server.sendmail(
                sendermail,receiver,message.as_string()
                )
                file = open("mailimg.txt","r")
                img = file.read()
                file.close()
                print("-----><-----\n{}-----><-----".format(img))
                print("*****************\nemail sent successfull.\nHave a nice day!")
        except:
            print("****************\nsomething went wrong.")
    
    
    elif s1 =="5":
    
        sendermail = input("*****\nsender e-mail(gmail):")

        sendermail += "@gmail.com"

        senderpassword=input("*****\npassword:")
        subject = input("subject:")

        receiver = input("*****\nreceiver e-mail(enter all the address):")
      
        
        switcher1 = input("*****\nWhich one do you prefer?\nto leave a little message by hand(m)\nenter the path that shows the document.(p)")

        if switcher1 == "m":
            content = input("*****\nenter your message:")

        elif switcher1 == "p":
            pathto = input("*****\nenter the path(it must be in .txt format.):")
            try:
                file = open(pathto,"r")
                content = file.read()
                file.close()
            except:
                print("-----------\n#something went wrong#\n#try to check out the file#\n#it can be missed or moved.#")
                continue
        else:
            print("#unvalid process code#")
            break

        message = MIMEMultipart("alternative")

        message["Subject"] = subject
        message["From"] = sendermail
        message["To"] = receiver

        message_content = MIMEText(content,"plain")
        message.attach(message_content)

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context)as server:
                server.login(sendermail,senderpassword)
                server.sendmail(
                sendermail,receiver,message.as_string()
                )
                file = open("mailimg.txt","r")
                img = file.read()
                file.close()
                print("-----><-----\n{}-----><-----".format(img))
                print("*****************\nemail sent successfull.\nHave a nice day!")
        except:
            print("****************\nsomething went wrong.")
   
    else:
        print("#unvalid input#")
