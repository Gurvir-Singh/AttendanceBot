import pyautogui
import time
import webbrowser
import datetime
import sched

def completeAttendance():
    webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLScUe1S-f9dt5pxNev5JLgEXsVWGRL6U4NIJVSe4HUKaNoP7Hw/viewform?authuser=1', new=2)
    time.sleep(2)
    pyautogui.moveTo(600, 475, duration=0.2)
    pyautogui.click()
    pyautogui.moveTo(600, 650, duration=0.2)
    pyautogui.click()

def checkForTime():
    isTime = False
    currentTime = datetime.datetime.now()
    while (not isTime):
        if (currentTime.hour == 12):
            if (currentTime.minute >= 18):
                break
        currentTime = datetime.datetime.now()
    
checkForTime()
completeAttendance()
