import schedule
import time
import fbchat
import random
from fbchat.models import *
from getpass import getpass

#Add your own custom messages by putting your message between "s and using the same format below
customMsgs = ["Good morning beautiful", "I'm too lazy", "To write messages on my own", "Custom message #4"]
#Put your own custom hour here
customTime = "4:20"

#Getting username & pwd
username = str(raw_input("Username: "))
passwrd = getpass()
client = fbchat.Client(username, passwrd)

#Getting recipient
name = str(raw_input("Name: "))
friends = client.searchForUsers(name)
friend = friends[0]

def morningMessage():
    #Sending message
    msg = random.choice(customMsgs)
    sent = client.send(Message(msg), thread_id=friend.uid, thread_type=ThreadType.USER)
    if sent:
        print("Message '" + msg + "' sent successfully!")
    else:
        client = fbchat.Client(username, passwrd)
        morningMessage()
    return

schedule.every().day.at(customTime).do(morningMessage)

while True:
    schedule.run_pending()
    time.sleep(60) #Wait one minute to check if it's #morningtime
