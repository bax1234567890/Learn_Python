# in terminal run "pip install pyautogui" on Linux: sudo apt-get install scrot

import pyautogui

# Take screenshot of display
screenshot = pyautogui.screenshot()
screenshot.save('/Users/ionbota/Documents/screenshot_example.png')