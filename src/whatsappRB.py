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
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
import randomTime

def morningMessage():
    #Sending message
    global driver
    global bae
    msg = random.choice(config.custom_morning_messages)
    baestr = str('"' + bae + '"')

    #Some Selenium stuff, don't bother
    try:
        pyperclip.copy(bae)
        searchbar = driver.find_elements_by_xpath('//*[@id="side"]/div[1]/div/label/input')[0]
        searchbar.click() #Click on searchbar
        searchbar.send_keys(Keys.CONTROL, 'v') #Search for contact for more speed
        x_arg = '//span[contains(@title,' + baestr + ')]'
        group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        group_title.click()
        time.sleep(0.1)
        pyperclip.copy(msg) #Copies random message to clipboard
        message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        message.send_keys(Keys.CONTROL, 'v') #Sends message from clipboard
        time.sleep(0.1)
        sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        sendbutton.click() #Presses send button
        searchbar.click() #Click on searchbar
        searchbar.send_keys(Keys.CONTROL, 'a') #Select all
        searchbar.send_keys(Keys.DELETE) #Delete searchbar content
        print("Message {} successfully sent to {}" .format(msg, bae))
    except:
        print("Problem sending, retrying...")
        morningMessage()
        pass
    return

#Getting username & pwd
bae = input("Name of your bae: ")
print("A popup view of WhatsApp web will now open,\nScan the QR code in the page via your app\nDon't close the popup")
time.sleep(5)

driver = webdriver.Chrome(
    '{}/chromedriver'.format(os.path.dirname(os.path.realpath('__file__'))))
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

randTimeHour, randTimeMinute = randomTime.new(config.custom_time_interval)

while True:
    if int(datetime.datetime.today().hour) == int(randTimeHour) and int(datetime.datetime.today().minute) == int(randTimeMinute):
        morningMessage()
        randTimeHour, randTimeMinute = randomTime.new(
            config.custom_time_interval)
    time.sleep(60) #Wait one minute to check if it's #morningtime
