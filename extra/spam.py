import pyautogui
import time

msg = "BHEJ NA MOVIEbhej na movie"
n = 10000
time.sleep(5)
for i in range(0,int(n)):
  pyautogui.typewrite(msg + '\n')