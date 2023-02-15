import pyautogui
import time
pyautogui.PAUSE=0.1
#wait few seconds before starting so we can alt+tab, unpause the game
time.sleep(6)

def hold_W (hold_time):
    pyautogui.FAILSAFE = False
    pyautogui.keyDown('w')
    time.sleep(hold_time)
    pyautogui.keyUp('w')
    pyautogui.FAILSAFE = True


def hold_S (hold_time):
    pyautogui.FAILSAFE = False
    pyautogui.keyDown('s')
    time.sleep(hold_time)
    pyautogui.keyUp('s')
    pyautogui.FAILSAFE = True

for x in range(5):
   #normal speed (8.45) / 2x Speed: 8.45/2
   hold_W(8.45/2)

   pyautogui.keyDown('space')
   time.sleep(0.5)
   pyautogui.keyDown('c')
   pyautogui.keyUp('space')
   pyautogui.keyUp('c')
   #normal speed: 14.3  / 2x Speed: 8.8
   hold_S(8.9)
   time.sleep(1)
   
   
   

