# Romance Breaker
##### "Is your girlfriend/boyfriend complaining that you wake up too late every morning or that you are not romantic enough but of course you're too lazy to change? I have a solution for you."  
  
Introducing *Romance Breaker*, a small python script which sends a custom morning message from a list to your significant other every morning at a given time range on Facebook Messenger or WhatsApp, now doesn't this sound great already?

### Most loved features:
  - You can still be lazy
  - You can still wake up late
  - Relationship improvement (I don't take any responsibility if Romance Breaker® doesn't improve relationship status)
  - Magic

---
# Facebook Messenger:
### Installation on PC

Romance breaker relies on a few things, here is what to do to get them:

- Python3 is needed get it from [here](https://www.python.org/downloads/)
###### For Linux:
Run these commands in your preferred terminal application  
```shell=
sudo apt-get install python-dev libxml2-dev libxslt1-dev zlib1g-dev
pip install fbchat bs4 
git clone https://github.com/lorcalhost/RomanceBreaker.git
```
###### For Windows
- Also install git from [here](https://git-scm.com/download/win)
- Make sure you run all the commands from git
```shell=
sudo pip install fbchat bs4 
git clone https://github.com/lorcalhost/RomanceBreaker.git
```

### Installation on Android 
As it was highly requested by the plebs without a raspberry pi:
From *Android* you will only be able to run the Facebook Messenger version, here are the instructions:
- First download and install [Termux from the Google Play Store](https://play.google.com/store/apps/details?id=com.termux)  
- Then run the following commands:

```termux-setup-storage``` and allow storage access  
```shell=
cd storage/downloads 
pkg install python git
pip install fbchat requests bs4 enum
git clone https://github.com/lorcalhost/RomanceBreaker.git
```
Please note that every time you restart your device, you will have to re run the commands in the *How to run* section

### How to run
###### Linux:
Simply ```cd RomanceBreaker``` and ```python RomanceBreaker.py```  
###### Android:
Simply ```cd storage/downloads/RomanceBreaker``` and ```python RomanceBreaker.py```  

For *Android* users: you will also need to press ```"ACQUIRE WAKELOCK"``` in the Termux notification to enable the script to run in the background without the process being killed

---

# WhatsApp and SMS
### Installation on PC

Romance breaker relies on a few things, here is what to do to get them:
- Python3 is needed get it from [here](https://www.python.org/downloads/)
- Chrome Driver get it from [here](https://chromedriver.storage.googleapis.com/index.html?path=2.44/) and unzip in the ```RomanceBreaker``` folder
- If you want to setup SMS you will need to have [Google messages](https://play.google.com/store/apps/details?id=com.google.android.apps.messaging) on your Android phone

###### For Linux:
Run these commands in your preferred terminal application  
```shell=
sudo apt-get install python-dev libxml2-dev libxslt1-dev zlib1g-dev xclip
sudo pip install selenium bs4 pyperclip
git clone https://github.com/lorcalhost/RomanceBreaker.git
```

###### For Windows
- Also install git from [here](https://git-scm.com/download/win)
- Make sure you run all the commands from git
```shell=
sudo pip install selenium bs4 pyperclip
git clone https://github.com/lorcalhost/RomanceBreaker.git
```

##### SMS mode is strongly not suggested, it's slow and buggy due to Google Messages nature
---
# Usage
First go to the program directory by typing in the terminal:
- From **PC:**  ```cd RomanceBreaker``` 
- From **Android:** ```cd storage/downloads/RomanceBreaker```  

Then run the script with the according argument:  
- For **WhatsApp version**: ```python romanceBreaker.py -w``` or ```python romanceBreaker.py whatsapp``` 
- For **Messenger version**: ```python romanceBreaker.py -m``` or ```python romanceBreaker.py messenger``` 
- For **SMS version**: ```python romanceBreaker.py -s``` or ```python romanceBreaker.py sms``` 

Also other arguments exist like:
- To open **user guide**: ```python romanceBreaker.py -h``` or ```python romanceBreaker.py help```  or ```python romanceBreaker.py man``` 
- To **update** the script: ```python romanceBreaker.py update```

**For *Android* users:** you will also need to press ```"ACQUIRE WAKELOCK"``` in the Termux notification to enable the script to run in the background withoutthe process being killed  
***Android right now only supports Facebook Messenger mode***
Simply ```cd RomanceBreaker``` and ```python WA-RomanceBreaker.py```  

# Custom messages/times setup
***Android** users may want to edit the ```config.py``` file with their preferred text editing app as the file will be in the Downloads folder of their devices*   
  
Simply open the ```config.py``` file with your preferred text editing app and follow the instructions there, I think I made them clear enough   
###### If you still cannot understand from the config.py file..
## Custom messages:


Replace the messages in between ```" "``` with your own custom messages, you can also add more custom messages by adding after the ```"``` of the last message a comma and a new message, always in between ```" "```s. 
If we want to add ```New custom message``` to the list below 
```python
custom_morning_messages = ["Good morning beautiful ♥♥♥"]
```
We just need to edit it like this:
```python
custom_morning_messages = ["Good morning beautiful ♥♥♥", "New custom message"]
```
## Custom time range: 

If we want to change the time range we have to edit this line:
```python
custom_time_interval = ["04:20", "16:20"]
```

Make sure the **hour** is always **two digits**

---

## Comments of people who are enjoying the effects of Romance Breaker:  
  
> My life has never been so great,  
> since I added this script with 1337  
> custom messages downloaded from the  
> dark net in bulk to my 24/7  
> running raspberry pi my life has  
> improved so much. Now my girlfriend  
> thinks I'm perfect, while I'm sleeping  
> peacefully and dreaming of waifus.  
Luca, 19 y/o, London  
---
###### This program was inspired by a real life critique, [@PreslavaKuzova](https://github.com/PreslavaKuzova)