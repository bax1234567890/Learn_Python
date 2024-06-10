import pyautogui

pyautogui.click(100, 100)
# Type characters
pyautogui.typewrite("Hello world!", interval=0.2)

# Type and go to left 2 characters
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=1)

# Keyboards we can use
keys = pyautogui.KEYBOARD_KEYS
print(keys)

# Use hotkeys in opened app
pyautogui.press(('f1'))
pyautogui.hotkey('command', 'r')

