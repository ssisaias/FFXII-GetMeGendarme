# FFXII - Get Me Gendarme

This script automates the running around and opening the chest to obtain the Gendarme ultimate shield in FF XII - The Zodiac Age

## Caution ⚠️
Please do not proceed if you don't know what you are doing, I am using pyautogui.FAILSAFE at the 'w' and 's' so the 
character can walk smoothly but this option may mess things around if we try to use the computer while the script is running. This is also the first time I try something with pyautogui.

## Motivations
1.  I want the Gendarme Shield
2. I don't want to install any memory address manipulators on my machine
3. None of the youtube videos manipulating the RNG worked for me
4. why not?

## Prerequisites

Pip:

`$ sudo apt install python3-pip`

pyautogui + Linux dependencies:

`$ python -m pip install pyautogui`

`$ sudo apt-get install python3-tk python3-dev`

## Considerations

- First thing to consider is adjusting the  `hold_W()` and ` hold_S()` functions. Test manually the amount of time you need to keep the key pressed and replicate on the function call. 
- Adjust the `for x in range(5)` loop to help check how will the repetitions behave. When comfortable go with higher numbers.
- Go to the Great Crystal, defeat Ultima if you have not yet, save the game on the crystal. As soon as you go back to Crystal Peak do not move anymore, start the script: `$ python3 getMeGerdame.py`


https://gist.github.com/ssisaias/180c9dd031ede2018a550f5cc50c894f
