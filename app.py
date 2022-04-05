from pynput import keyboard, mouse
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener, KeyCode
import asyncio

mouse = Controller()
def show(key):
  
    print('\nYou Entered {0}'.format(key))
    if isinstance(key, KeyCode):
        if key.char == 'q':
            mouse.position = (325, 625)
            print("325, 625")
            mouse.press(Button.left)
            mouse.release(Button.left)
        elif key.char == 'w':
            mouse.position = (1075, 625)
            print("1075, 625")
            mouse.press(Button.left)
            mouse.release(Button.left)
        elif key.char == 'a':
            mouse.position = (325, 750)
            print("325, 750")
            mouse.press(Button.left)
            mouse.release(Button.left)
        elif key.char == 's':
            mouse.position = (1075, 750)
            print("1075, 750")
            mouse.press(Button.left)
            mouse.release(Button.left)
        elif key.char == 'e':
            mouse.position = (1400, 235)
            print(1400, 235)
            mouse.press(Button.left)
            mouse.release(Button.left)
    if key == Key.delete:
        # Stop listener
        return False
  
# Collect all event until released
with Listener(on_press = show) as listener:   
    listener.join()



# Read pointer position
print('The current pointer position is {0}'.format(mouse.position))

