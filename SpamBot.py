import win32com.client as comclt
import keyboard
import time
wsh= comclt.Dispatch("WScript.Shell")
wsh.AppActivate("Notepad") # select another application

count = 100000

while True:  # making a loop
    if keyboard.is_pressed('.'):
        wsh.SendKeys("{ENTER}")
        n = 0
        while count > n:
            if keyboard.is_pressed('n'):
                break
            time.sleep(0.1)
            wsh.SendKeys("Hei Cecilie <3")
            wsh.SendKeys("{ENTER}")