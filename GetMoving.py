import datetime
import time
from CustomSound import play_custom_sound


print("Enter a mode (Gaming or Coding)")
#If mode is coding, then set a variable time for each alarm     
#If mode is gaming, set a constant 30 minute timer 



mode = input(">> ")
if (mode == 'Gaming'):
    for i in range(0, 1800):
        time.sleep(1)
elif (mode == 'Coding'):
    print("Enter the time you'd like to take for this problem")
    minutes = input(">> ")
    seconds = int(minutes) * 60
    for i in range(0, seconds):
        time.sleep(1)
userInput = ''
while (userInput != 'S'):
    # userInput = input("Input S to stop: ")
    # Make noise until user input 
    play_custom_sound("WhoseGonnaCarryTheBoats.wav")


