#!/usr/bin/python3
import sys
import os
import config

command = "python"
if config.currentOS is "Linux":
    command += "3 src/"
else:
    command += " src\\"


def prnthelp():
    print("Welcome to the RomanceBreaker user guide\nPlease refer to the Github page for detailed setup instructions")
    print("\nList of commands:\nwhatsapp or -w ---> launches RomanceBreaker in WhatsApp mode\nmessenger or -m ---> launches RomanceBreaker in Messenger mode\nsms or -s ---> launches RomanceBreaker in SMS mode\ntelegram or -t ---> launches RomanceBreaker in Telegram mode")
    print("help or -h or man ---> Launches user guide\nupdate ---> Updates RomanceBreaker from the github repo")


try:
    if str(sys.argv[1]) == "whatsapp" or str(sys.argv[1]) == "-w":
        print("WHATSAPP MODE")
        os.system("{}whatsappRB.py" .format(command))
    elif str(sys.argv[1]) == "messenger" or str(sys.argv[1]) == "-m":
        print("MESSENGER MODE")
        os.system("{}messengerRB.py" .format(command))
    elif str(sys.argv[1]) == "sms" or str(sys.argv[1]) == "-s":
        print("SMS MODE")
        os.system("{}smsRB.py" .format(command))
    elif str(sys.argv[1]) == "telegram" or str(sys.argv[1]) == "-t":
        print("TELEGRAM MODE")
        os.system("{}telegramRB.py" .format(command))
    elif str(sys.argv[1]) == "help" or str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "man":
        prnthelp()
    elif str(sys.argv[1]) == "update":
        os.system("git pull")
except:
    print("Invalid arguments\nTry running {} romanceBreaker.py -h to show the list of commands" .format(command))
