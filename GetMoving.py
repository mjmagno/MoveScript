import datetime
import time
import threading
import os

from CustomSound import play_custom_sound

def alarm(sound_file_path):
    t = threading.current_thread()
    while (getattr(t,"do_run",True)):
        play_custom_sound(sound_file_path)

# Accepts a time in second and then puts program to sleep for that long 
#TODO "1.0 minutes remaining"
#TODO remove ".0" from minutes remaining 
def sleep (timer) :
    for i in range(0, timer):
        if (i % 60 == 0):
            print(str(timer / 60 - i / 60) + " minutes remaining")
        time.sleep(1)
    return


if __name__ == "__main__":
    print("Enter a mode (Gaming or Coding)")
    #If mode is coding, then set a variable time for each alarm     
    #If mode is gaming, set a constant 30 minute timer 

    mode = (input(">> ")).lower()
    userInput = ""
    minutes = 0
    if (mode == 'gaming'):
        minutes = 30
    while (userInput != 'e'):
        if (mode == 'coding'):
            print("Enter the time you'd like to take for this problem")
            minutes = input(">> ")
        seconds = int(minutes) * 60
        sleep(seconds)
        t1 = threading.Thread(target=alarm,args=("WhoseGonnaCarryTheBoats.wav",))
        t1.start()
        # Not sure if I like how this is implented, a while seems weird but using an if statement
        # will result in the program infinite looping if the user misinputs
        while (input("Enter S to stop ").lower() == 'S'):
            t1.do_run = True
        t1.do_run = False
        print("Enter E to exit or press another key to continue")
        userInput = input(">> ").lower()


#TODO
# Add a way to pause timer
# Make input printing consistent 
# Convert time remaining to int 
# Error handling
# Different alarms 
# Bug with starting a thread again when looping code
# Automated testing? 