import schedule
import time
import fbchat
import random
from fbchat.models import *
from getpass import getpass

#Add your own custom messages by putting your message between "s and using the same format below
customMsgs = ["Good morning beautiful", "I'm too lazy", "To write messages on my own", "Custom message #4"]

#Getting username & pwd
username = str(raw_input("Username: "))
client = fbchat.Client(username, getpass())

#Getting recipient
name = str(raw_input("Name: "))
friends = client.searchForUsers(name)
friend = friends[0]

def morningMessage():
    #Finally sending
    print("DONE")
    msg = random.choice(customMsgs)
    sent = client.send(Message(msg), thread_id=friend.uid, thread_type=ThreadType.USER)
    if sent:
        print("Message '" + msg + "' sent successfully!")
    return

schedule.every().day.at("8:00").do(morningMessage)

while True:
    schedule.run_pending()
    time.sleep(60) # Wait one minute