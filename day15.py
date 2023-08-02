# Day 15 Python programming

# Python programe for say diff msg according to time using time module

import time #time is pre installed module

# https://docs.python.org/3/library/time.html#time.strftime

time_hours = int(time.strftime('%H'))
time_min = int(time.strftime('%M'))
time_sec = int(time.strftime('%S'))

print("The time right now is " + str(time_hours) + ":" + str(time_min) + ":" + str(time_sec))

if(time_hours < 12):
    print("\nVery Very Good Morning Sir.")
elif(time_hours >= 12 , time_hours < 18):
    print("\nGood Afternoon Sir.")
else:
    print("\nGood Evening.")