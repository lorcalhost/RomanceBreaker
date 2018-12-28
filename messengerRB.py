# -*- coding: utf-8 -*- 
import time
import datetime
import fbchat
import random
from fbchat.models import ThreadType, Message
from getpass import getpass
import config

randTimeHour = 0
randTimeMinute = 0

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

def newRandTime():
    global randTimeHour
    global randTimeMinute
    randTimeHour = random.randint(int(config.custom_time_interval[0][0:2]), int(config.custom_time_interval[1][0:2]))
    if int(randTimeHour) == int(config.custom_time_interval[1][0:2]):
        randTimeMinute = random.randint(0, int(config.custom_time_interval[1][3:5]))
    elif int(randTimeHour) == int(config.custom_time_interval[0][0:2]):
        randTimeMinute = random.randint(int(config.custom_time_interval[1][3:5]), 59)
    else:
        randTimeMinute = random.randint(0, 59)
    print("I'll send a message at {}:{}..." .format(randTimeHour.zfill(2), randTimeMinute.zfill(2)))
    return

newRandTime()

while True:
    if int(datetime.datetime.today().hour) == int(randTimeHour) and int(datetime.datetime.today().minute) == int(randTimeMinute):
        morningMessage()
        newRandTime()
    time.sleep(60) #Wait one minute to check if it's #morningtime