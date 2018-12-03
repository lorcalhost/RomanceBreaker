import time
import datetime
import fbchat
import random
from fbchat.models import *
from getpass import getpass

#Add your own custom messages by putting your message between "s and using the same format below
customMsgs = ["Good morning beautiful", "I'm too lazy", "To write messages on my own", "Custom message #4"]
#Put your own custom time interval here, make sure the hour is always two digits
customTimeInterval = ["04:20", "16:20"]

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
    msg = random.choice(customMsgs)
    global client
    global bae
    sent = client.send(Message(msg), thread_id=bae.uid, thread_type=ThreadType.USER)
    if sent:
        print("Message '" + msg + "' sent successfully!\nWaiting for next scheduled time...")
    else:
        global username
        global passwrd
        client = fbchat.Client(username, passwrd)
        morningMessage()
    return

def newRandTime():
    global customTimeInterval
    global randTimeHour
    global randTimeMinute
    randTimeHour = random.randint(int(customTimeInterval[0][0:2]), int(customTimeInterval[1][0:2]))
    if int(randTimeHour) == int(customTimeInterval[1][0:2]):
        randTimeMinute = random.randint(0, int(customTimeInterval[1][3:5]))
    elif int(randTimeHour) == int(customTimeInterval[0][0:2]):
        randTimeMinute = random.randint(int(customTimeInterval[1][3:5]), 59)
    else:
        randTimeMinute = random.randint(0, 59)
    print("I'll send a message at " + str(randTimeHour).zfill(2) + ":" + str(randTimeMinute).zfill(2) + "...")
    return

newRandTime()

while True:
    if int(datetime.datetime.today().hour) == int(randTimeHour) and int(datetime.datetime.today().minute) == int(randTimeMinute):
        morningMessage()
        newRandTime()
    time.sleep(60) #Wait one minute to check if it's #morningtime
