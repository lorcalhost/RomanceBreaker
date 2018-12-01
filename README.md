# Romance Breaker
##### "Is your girlfriend/boyfriend complaining that you wake up too late every morning or that you are not romantic enough but you're to lazy to change? I have a solution."

Romance Breaker is small python script which sends a custom morning message from a list to your significant other every morning at a given time, now doesn't this sound great already?

### Most loved features:
  - You can still be lazy
  - You can still wake up late
  - Relationship improvement (I don't take any responsibility if Romance Breaker doesn't improve relationship status)
  - Magic

# Installation

Romance breaker relies on a few things, here is what to do to get them:
```sh
sudo apt-get install python-dev libxml2-dev libxslt1-dev zlib1g-dev
sudo pip install fbchat bs4 schedule
```
## Custom messages setup
I guess you also want to send custom messages, so here we go:
On line 9 replace the messages in between ```" "``` with your own custom messages, you can also add more than three by adding after the ```"``` of the last message a comma and a new message, always in between ```" "```s
If we want to add ```NewCustomMessage``` to the list below
```python
9 customMsgs = ["Good morning beautiful", "I'm too lazy", "To write messages on my own"]
```
We just need to edit it like this:
```python
9 customMsgs = ["Good morning beautiful", "I'm too lazy", "To write messages on my own", "NewCustomMessage"]
```
## Custom time setup
To change the time at which the #MorningText should be sent just change line 11:
```python
11 customTime = "4:20"
```
## Comments of people who are enjoying the effects of Romance Breaker:  
  
> My life has never been so great,
> since I added this script to my
> 24/7 running raspberry pi my life has
> improved so much. Now my girlfriends
> thinks I'm perfect, while I'm sleeping
> peacefully and dreaming of waifus
> Luca, 19 y/o, London
