# GUI automation is like robotic arm and can do anything
import pyautogui
# https://pyautogui.readthedocs.io/en/latest/
# Y = Vertical
# X = Horizontal
# multiple assigment to display screen size
screen_width, screen_height = pyautogui.size()
print(f"Screen width: {screen_width}, Screen height: {screen_height}")

# mouse coordinates
print(pyautogui.position())
pyautogui.moveTo(10, 10, duration=1.5)

# move mouse to any direction
pyautogui.moveRel(20, 0)
pyautogui.moveRel(0, -100)

# click to specific mouse coordinates
pyautogui.click(x=141, y=15)
pyautogui.doubleClick(x=191, y=19)
pyautogui.rightClick(x=233, y=15)
pyautogui.middleClick(x=363, y=21)