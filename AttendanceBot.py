import pyautogui
import time
import webbrowser
import datetime
import sched
import sys

def completePEAttendance(debug = False):
    pass

def completeHistoryAttendance(debug = False):
    webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLSdp_e8L30WpWHkLwJtflMyK2RDg3axs8TTXmwJWHyaAZLATgw/viewform?authuser=1', new=2)
    time.sleep(2)
    pyautogui.moveTo(600, 725, duration=0.2)
    if (not debug):
        pyautogui.click()
    pyautogui.moveTo(600, 810, duration=0.2)
    if (not debug):
        pyautogui.click()

def completePhysicsAttendance(debug = False):
    webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLSdp_e8L30WpWHkLwJtflMyK2RDg3axs8TTXmwJWHyaAZLATgw/viewform?authuser=1', new=2)
    time.sleep(2)
    pyautogui.moveTo(600, 725, duration=0.2)
    if (not debug):
        pyautogui.click()
    pyautogui.moveTo(600, 810, duration=0.2)
    if (not debug):
        pyautogui.click()
        
def completeAdvisoryAttendance(debug = False):
    webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLScUe1S-f9dt5pxNev5JLgEXsVWGRL6U4NIJVSe4HUKaNoP7Hw/viewform?authuser=1', new=2)
    time.sleep(2)
    pyautogui.moveTo(600, 475, duration=0.2)
    if (not debug):
        pyautogui.click()
    pyautogui.moveTo(600, 650, duration=0.2)
    if (not debug):
        pyautogui.click()

def checkForTime(hourToCheck, minuteToCheck):
    isTime = False
    currentTime = datetime.datetime.now()
    while (not isTime):
        if (currentTime.hour == hourToCheck):
            if (currentTime.minute >= minuteToCheck):
                break
        currentTime = datetime.datetime.now()

if (sys.argv[1] == "A" or sys.argv[1] == "a"):
    checkForTime(7, 20)
    completeHistoryAttendance(True)
elif (sys.argv[1] == "B" or sys.argv[1] == "b"):
    completePEAttendance(True)
else:
    pass
checkForTime(8, 53)
completePhysicsAttendance(True)
checkForTime(12, 18)
completeAdvisoryAttendance(True)
