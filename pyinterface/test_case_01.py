import serial
import time
import pyautogui

ser = serial.Serial('COM6', 9600)
time.sleep(2)

data =[]                       # empty list to store the data
while(True):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode
    string = string_n.rstrip() # remove \n and \r
    #flt = string        # convert string to float
    #print(flt)
    #data.append(flt)           # add to the end of data list
    time.sleep(0.1)            # wait (sleep) 0.1 seconds
    if (string == "yes"):
        pyautogui.press('right')
#ser.close()




