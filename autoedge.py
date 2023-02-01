import pyautogui
from time import sleep

pyautogui.click(1232,296)
pyautogui.write('oi')
pyautogui.click(1656,290, duration=1)

for i in range(31):
    i = i + 1
    pyautogui.click(1247,116, duration=0.2)
    pyautogui.write('k')
    pyautogui.click(1741,121)