import serial
import time
import pyautogui

ser = serial.Serial('COM5', 115200)
time.sleep(2)

data =[]                       # empty list to store the data
while(True):
    received = ser.readline()         # read a byte string
    strip = received.rstrip()
    decod = strip.decode('utf-8')
    if (decod == "right"):
        pyautogui.press('right')

    elif (decod == "left"):
        pyautogui.press('left')
