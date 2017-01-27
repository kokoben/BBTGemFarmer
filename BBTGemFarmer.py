import time
from pywinauto import application
from autopy.key import *

def inputCommmand(command, time_to_hold=0):
    toggle(command, True)
    if time_to_hold != 0:
        time.sleep(time_to_hold)
    toggle(command, False)

bbtApp = application.Application()
bbtApp.start_(r'C:\Program Files (x86)\Steam\SteamApps\common\BattleBlock Theater\BattleBlockTheater.exe')

time.sleep(25)
# get to the main menu.
inputCommmand(K_RETURN)
time.sleep(1)
# select local game.
inputCommmand(K_RETURN)
time.sleep(1)
# toggle down to arena mode.
inputCommmand(K_DOWN)
time.sleep(0.5)
# select arena mode.
inputCommmand(K_RETURN)
time.sleep(1)
# select vs. mode.
inputCommmand(K_RETURN)
time.sleep(1)
# toggle down twice then left once to highlight Feature mode.
inputCommmand(K_DOWN)
time.sleep(0.5)
inputCommmand(K_DOWN)
time.sleep(0.5)
inputCommmand(K_LEFT)
time.sleep(1)
# select Feature mode.
inputCommmand(K_RETURN)
time.sleep(1)
# press Enter four times to proceed through Player Setup.
inputCommmand(K_RETURN)
time.sleep(0.8)
inputCommmand(K_RETURN)
time.sleep(0.8)
inputCommmand(K_RETURN)
time.sleep(0.8)
inputCommmand(K_RETURN)
time.sleep(5.5)
# walk towards the right until you are in front of the first level door.
inputCommmand(K_RIGHT, 0.95)
time.sleep(1)
while True:
    # enter the first level door.
    inputCommmand(K_RETURN, 1)
    time.sleep(2)
    inputCommmand(K_ESCAPE, 1)
    time.sleep(1)
    inputCommmand(K_CONTROL, 1)
    time.sleep(8)
    # walk towards the right to the exit gate. (first level)
    inputCommmand(K_RIGHT, 2)
    time.sleep(16)
    # walk towards the right to the exit gate. (second level)
    inputCommmand(K_RIGHT, 2)
    time.sleep(16)
    # walk towards the right to the exit gate. (third level)
    inputCommmand(K_RIGHT, 2)
    time.sleep(16)
    # back at the level lobby, walk back to the entrance to the first level.
    inputCommmand(K_LEFT, 1.4)

