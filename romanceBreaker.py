#!/usr/bin/python3
import sys
import os

def prnthelp():
    print("Welcome to the RomanceBreaker user guide\nPlease refer to the Github page for detailed setup instructions")
    print("\nList of commands:\nwhatsapp or -w ---> launches RomanceBreaker in WhatsApp mode\nmessenger or -m ---> launches RomanceBreaker in Messenger mode\nsms or -s ---> launches RomanceBreaker in SMS mode")
    print("help or -h or man ---> Launches user guide\nupdate ---> Updates RomanceBreaker from the github repo")
try:
    if str(sys.argv[1]) == "whatsapp" or str(sys.argv[1]) == "-w":
        print("WHATSAPP MODE")
        os.system("python whatsappRB.py")
    elif str(sys.argv[1]) == "messenger" or str(sys.argv[1]) == "-m":
        print("MESSENGER MODE")
        os.system("python messengerRB.py")
    elif str(sys.argv[1]) == "sms" or str(sys.argv[1]) == "-s":
        print("SMS MODE")
        os.system("python smsRB.py")
    elif str(sys.argv[1]) == "help" or str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "man":
        prnthelp()
    elif str(sys.argv[1]) == "update":
        os.system("git pull")
except:
    print("Invalid arguments\nRun python romanceBreaker.py -h to look at the commands manual")