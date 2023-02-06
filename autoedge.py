import pyautogui

pyautogui.click(1232,296)
pyautogui.write('2')
pyautogui.click(1656,290)

for i in range(15):
    i = i + 1
    pyautogui.click(1247,116, duration=0.2)
    pyautogui.write('M')
    pyautogui.click(1741,121)
    #pyautogui.click(1146,122)


    