# -*- coding: utf-8 -*- 
import time
import datetime
import random
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
import randomTime

#Getting username & pwd
client = TelegramClient(config.telegram_username,
                        config.tg_api_id, config.tg_api_hash)
client.start(config.telegram_phone, config.telegram_password)

#Getting recipient
name = input("Username of your bae: ")
friends = client.searchForUsers(name)
bae = friends[0]


def morningMessage():
    #Sending message
    msg = random.choice(config.custom_morning_messages)
    global client
    global bae
    sent = client.send_message(bae, msg)
    if sent:
        print("Message '{}' sent successfully!\nWaiting for next scheduled time..." .format(msg))
    else:
        print("There was an error trying to send the message")
    return


randTimeHour, randTimeMinute = randomTime.new(config.custom_time_interval)

while True:
    if int(datetime.datetime.today().hour) == int(randTimeHour) and int(datetime.datetime.today().minute) == int(randTimeMinute):
        morningMessage()
        randTimeHour, randTimeMinute = randomTime.new(
            config.custom_time_interval)
    time.sleep(60)  # Wait one minute to check if it's #morningtime
