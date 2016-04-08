# -*- coding: cp950 -*-
import time
import os
import sys
import pyautogui

os.chdir(os.path.dirname(os.path.realpath(__file__)))
directory = 'mouse_recorder'
try:
    session_name = sys.argv[1]
except:
    print 'you must enter a name for the session\nfor example: python replay.py session_name'
    sys.exit()
dir_path = os.path.join(os.getcwd(), directory, session_name)

file_name = 'history.txt'
file_path = os.path.join(dir_path, file_name)
#print dir_path

# open the recording file
with open(file_path, 'r') as f:
    steps = f.readlines()

# clean steps
new_steps = []
for step in steps:
    new_step = []
    for i in step.split(','):
        new_step.append(i.strip('\n'))
    new_steps.append(new_step)


# start moving mouse cursor
t_last = float(new_steps[0][-1])

for step in new_steps:

    if step[0] == 'left_down':
        time.sleep(float(step[-1]) - t_last)
        pyautogui.moveTo(int(step[1]), int(step[2]))
        pyautogui.mouseDown(button='left')
        t_last = float(step[-1])

    if step[0] == 'left_up':
        time.sleep(float(step[-1]) - t_last)
        pyautogui.moveTo(int(step[1]), int(step[2]))
        pyautogui.mouseUp(button='left')
        t_last = float(step[-1])

    if step[0] == 'right_down':
        time.sleep(float(step[-1]) - t_last)
        pyautogui.moveTo(int(step[1]), int(step[2]))
        pyautogui.mouseDown(button='right')
        t_last = float(step[-1])

    if step[0] == 'right_up':
        time.sleep(float(step[-1]) - t_last)
        pyautogui.moveTo(int(step[1]), int(step[2]))
        pyautogui.mouseUp(button='right')
        t_last = float(step[-1])

    if step[0] == 'done':
        print 'End autorun'
        sys.exit()
