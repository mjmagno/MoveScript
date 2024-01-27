import datetime
import time
import threading
import os

from CustomSound import play_custom_sound

def alarm(sound_file_path):
    t = threading.current_thread()
    while (getattr(t,"do_run",True)):
        # Need to listen, not sure if the sound is overlapping 
        play_custom_sound(sound_file_path)

# Accepts a time in second and then puts program to sleep for that long 
def sleep (timer) :
    for i in range(0, timer):
        time.sleep(1)






print("Enter a mode (Gaming or Coding)")
#If mode is coding, then set a variable time for each alarm     
#If mode is gaming, set a constant 30 minute timer 


t1 = threading.Thread(target=alarm,args=("WhoseGonnaCarryTheBoats.wav",))
mode = (input(">> ")).lower()
if (mode == 'gaming'):
    sleep(1800)
elif (mode == 'coding'):
    print("Enter the time you'd like to take for this problem")
    minutes = input(">> ")
    seconds = int(minutes) * 60
    sleep(seconds)
t1.start()
while (input("Enter S to stop ").lower() == 'S'):
    t1.do_run = True
    # Make noise until user input 
t1.do_run = False


