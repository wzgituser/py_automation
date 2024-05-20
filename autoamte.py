import pyautogui
import os
list_a = []
# pyautogui library
# current screen resolution width and height
print(pyautogui.size())
# current mouse x and y
a = pyautogui.position()
list_a.append(a)
print(list_a[0][0])
print(f'--------lista:{list_a}')
# y&x if within the screen
print(pyautogui.onScreen(a.x, a.y))
# mouse move to in sec's
b = pyautogui.moveTo(list_a[0][0], list_a[0][1], duration=1)
print(b)
c = pyautogui.moveRel(list_a[0][0] - 100, list_a[0][1] + 50)
print(pyautogui.position(c))
# kybord automation
# pyautogui.write('Hello world!', interval=3.25)
d = pyautogui.screenshot('screen.png')
print(d)
e = pyautogui.write("print('night time')", interval=1)
print(e)
