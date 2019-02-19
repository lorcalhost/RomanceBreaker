# -*- coding: utf-8 -*- 
import time
import datetime
import fbchat
import random
from fbchat.models import ThreadType, Message
from getpass import getpass
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
import randomTime


#Getting username & pwd
username = input("Username: ")
passwrd = getpass()
client = fbchat.Client(username, passwrd)

#Getting recipient
name = input("Username of your bae: ")
friends = client.searchForUsers(name)
bae = friends[0]

def morningMessage():
    #Sending message
    msg = random.choice(config.custom_morning_messages)
    global client
    global bae
    sent = client.send(Message(msg), thread_id=bae.uid, thread_type=ThreadType.USER)
    if sent:
        print("Message '{}' sent successfully!\nWaiting for next scheduled time..." .format(msg))
    else:
        global username
        global passwrd
        client = fbchat.Client(username, passwrd)
        morningMessage()
    return

randTimeHour, randTimeMinute = randomTime.new(config.custom_time_interval)

while True:
    if int(datetime.datetime.today().hour) == int(randTimeHour) and int(datetime.datetime.today().minute) == int(randTimeMinute):
        morningMessage()
        randTimeHour, randTimeMinute = randomTime.new(
            config.custom_time_interval)
    time.sleep(60) #Wait one minute to check if it's #morningtime
