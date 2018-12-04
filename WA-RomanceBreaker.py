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

#Add your own custom messages by putting your message between "s and using the same format below
customMsgs = ["Good morning beautiful ♥♥♥", "I'm too lazy", "To write messages on my own", "Custom message #4"]
#Put your own custom time interval here, make sure the hour is always two digits
customTimeInterval = ["04:20", "16:20"]

randTimeHour = 0
randTimeMinute = 0

#Getting username & pwd
bae = input("Name of your bae: ")
bae = str('"' + bae + '"')
print("A popup view of WhatsApp web will now open,\nScan the QR code in the page via your app\nDon't close the popup")
time.sleep(5)

driver = webdriver.Chrome('./chromedriver')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

def morningMessage():
    #Sending message
    global driver
    global bae
    msg = random.choice(customMsgs)
    pyperclip.copy(msg) #Copies random message to clipboard

    #Some Selenium stuff, don't bother
    x_arg = '//span[contains(@title,' + bae + ')]'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()
    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    message.send_keys(Keys.CONTROL, 'v') #Sends message from clipboard
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sendbutton.click() #Presses send button
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
