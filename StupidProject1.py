import os
import time
import smtplib
import webbrowser
import pyperclip
import requests
from bs4 import BeautifulSoup

site_name = input("What is the site URL that you want to get the name from?\n Ex. https://namemc.com/name/Qh4\n >>")
if os.name == 'nt':
    os.system('cls')
else:
    os.system("clear")
your_email = input("What is the name of your e-mail?\n >>")
if os.name == 'nt':
    os.system('cls')
else:
    os.system("clear")
your_password = input("What is the password for your email?\nThis won't be seen by anyone else.\n >>")
if os.name == 'nt':
    os.system('cls')
else:
    os.system("clear")

data = requests.get(site_name)

soup = BeautifulSoup(data.text, 'html.parser')

username = soup.find(class_='my-1 px-3 text-center text-nowrap text-ellipsis').get_text()
days = soup.find(id='countdown-days').get_text()
hours = soup.find(id='countdown-hours').get_text()
minutes = soup.find(id='countdown-minutes').get_text()
seconds = soup.find(id='countdown-seconds').get_text()

d = int(days)
h = int(hours)
m = int(minutes)
s = int(seconds)

due_date = d * 86400 + h * 3600 + m * 60 + s

while due_date > 0:
    try:
        when_to_stop = due_date
    except KeyboardInterrupt:
        break
    except:
        print("Not a number!")

    while due_date > 0:
        data = requests.get(site_name)

        soup = BeautifulSoup(data.text, 'html.parser')

        username = soup.find(class_='my-1 px-3 text-center text-nowrap text-ellipsis').get_text()
        days = soup.find(id='countdown-days').get_text()
        hours = soup.find(id='countdown-hours').get_text()
        minutes = soup.find(id='countdown-minutes').get_text()
        seconds = soup.find(id='countdown-seconds').get_text()
        d = int(days)
        h = int(hours)
        m = int(minutes)
        s = int(seconds)
        due_date = d * 86400 + h * 3600 + m * 60 + s
        time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
        print(time_left)
        time.sleep(10)
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system("clear")
        if due_date < 300:
            def send_email(subject, msg):
                try:
                    server = smtplib.SMTP('smtp.gmail.com:587')
                    server.ehlo()
                    server.starttls()
                    server.login(your_email,your_password)
                    message = 'Subject: {}\n\n{}'.format(subject, msg)
                    server.sendmail(your_email,your_email, message)
                    server.quit()
                    print("Email has been sent.")
                except:
                    print("Email failed to send.")


            subject = "Minecraft Username"
            msg = "You've got 5mins bud. Get on your computer."
            send_email(subject, msg)
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system("clear")
            while due_date > 0:
                data = requests.get(site_name)

                soup = BeautifulSoup(data.text, 'html.parser')

                username = soup.find(class_='my-1 px-3 text-center text-nowrap text-ellipsis').get_text()
                days = soup.find(id='countdown-days').get_text()
                hours = soup.find(id='countdown-hours').get_text()
                minutes = soup.find(id='countdown-minutes').get_text()
                seconds = soup.find(id='countdown-seconds').get_text()
                d = int(days)
                h = int(hours)
                m = int(minutes)
                s = int(seconds)
                due_date = d * 86400 + h * 3600 + m * 60 + s
                time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
                print(time_left)
                time.sleep(10)
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system("clear")
                if due_date < 20:
                    print("Ctrl + V into the change username part of the window that shows up in your browser.")
                    pyperclip.copy(username)
                    webbrowser.open('https://my.minecraft.net/en-us/profile/')
                    time.sleep(15)
                    print("Thank you for wasting 3 days of my life for this useless code that I will never use.")