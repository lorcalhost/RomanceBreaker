# Romance Breaker
##### "Is your girlfriend/boyfriend complaining that you wake up too late every morning or that you are not romantic enough but of course you're too lazy to change? I have a solution for you."

Romance Breaker is a small python script which sends a custom morning message from a list to your significant other every morning at a given time on Facebook Messenger, now doesn't this sound great already?

### Most loved features:
  - You can still be lazy
  - You can still wake up late
  - Relationship improvement (I don't take any responsibility if Romance Breaker® doesn't improve relationship status)
  - Magic

---

# Installation on linux

Romance breaker relies on a few things, here is what to do to get them:
```sh
sudo apt-get install python-dev libxml2-dev libxslt1-dev zlib1g-dev
sudo pip install fbchat bs4 schedule
```
Also don't forget to ```git clone https://github.com/lorcalhost/RomanceBreaker.git```

# Installation on Android 
As it was highly requested by the plebs without a raspberry pi:
First download and install [Termux from the Google Play Store](https://play.google.com/store/apps/details?id=com.termux)  
Then run the following commands:   
```sh
pkg install python git
pip install fbchat schedule
git clone https://github.com/lorcalhost/RomanceBreaker.git
```
Please note that every time you restart your device, you will have to re run the commands in the *How to run* section

# How to run
Simply ```cd RomanceBreaker``` and ```python RomanceBreaker.py```  
For *Android* users: you will also need to press ```"ACQUIRE WAKELOCK"``` in the Termux notification to enable the script to run in the background without the process being killed

---

## Custom messages setup
I guess you also want to send custom messages, so here we go:. 
On line 9 replace the messages in between ```" "``` with your own custom messages, you can also add more than three by adding after the ```"``` of the last message a comma and a new message, always in between ```" "```s. 
If we want to add ```NewCustomMessage``` to the list below. 
```python
9 customMsgs = ["Good morning beautiful", "I'm too lazy", "To write messages on my own"]
```
We just need to edit it like this:
```python
9 customMsgs = ["Good morning beautiful", "I'm too lazy", "To write messages on my own", "NewCustomMessage"]
```
## Custom time setup
To change the time at which the #MorningText should be sent just change line 11 with your custom interval:
```python
customTimeInterval = ["04:20", "16:20"]
```


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
>  
> Luca, 19 y/o, London
