# -*- coding: utf-8 -*-
import random

def new(interval):
    hour = random.randint(int(interval[0][0:2]), int(interval[1][0:2]))
    if int(hour) == int(interval[1][0:2]):
        minute = random.randint(0, int(interval[1][3:5]))
    elif int(hour) == int(interval[0][0:2]):
        minute = random.randint(int(interval[1][3:5]), 59)
    else:
        minute = random.randint(0, 59)
    print("I'll send a message at {}:{}..." .format(
        hour.zfill(2), minute.zfill(2)))
    return hour, minute
