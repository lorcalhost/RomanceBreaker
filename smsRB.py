# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import datetime
import random
import pyperclip
import config

def morningMessage():
    #Sending message
    global driver
    global bae
    msg = random.choice(config.custom_morning_messages)
    try:
        pyperclip.copy(bae)
        searchbar = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[3]')[0]
        searchbar.click()
        time.sleep(1)
        newmessage = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/input')
        newmessage.send_keys(Keys.CONTROL, 'v')
        msg = random.choice(config.custom_morning_messages)
        pyperclip.copy(msg)
        time.sleep(5)
        newmessage.send_keys(Keys.ENTER)
        time.sleep(6.5)
        message = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div/div[2]/div/div[3]/div/div/div[3]/div[2]/div[1]/div/div[2]/div/div[1]')[0]
        message.send_keys(Keys.CONTROL, 'v')
        message.send_keys(Keys.ENTER)
        print("Message " + msg + " successfully sent to" + bae)
    except:
        print("Problem sending, retrying...")
        morningMessage()
        pass
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
    print("I'll send a message at " + str(randTimeHour).zfill(2) + ":" + str(randTimeMinute).zfill(2) + "...")
    return

#Getting username & pwd
bae = input("Name of your bae: ")
print("A popup view of Google Messages will now open,\nScan the QR code in the page via your app\nDon't close the popup")
time.sleep(5)

driver = webdriver.Chrome('./chromedriver')
driver.get("https://messages.android.com/")
wait = WebDriverWait(driver, 600)

randTimeHour = 0
randTimeMinute = 0
newRandTime()

while True:
    if int(datetime.datetime.today().hour) == int(randTimeHour) and int(datetime.datetime.today().minute) == int(randTimeMinute):
        morningMessage()
        newRandTime()
    time.sleep(60) #Wait one minute to check if it's #morningtime