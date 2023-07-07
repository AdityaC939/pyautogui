import pyautogui
import time

# Delay for user to focus on the desired window
time.sleep(2)

# Press and hold Command, press Space, then release both keys
pyautogui.keyDown('command')
pyautogui.press('space')
pyautogui.keyUp('command')

# Delay for the Spotlight Search to appear
time.sleep(1)

# Type 'chrome' and press Enter
pyautogui.typewrite('chrome')
pyautogui.press('enter')

# Delay for Chrome to open
time.sleep(2)

# Press and hold Command, press 'L', then release both keys
pyautogui.keyDown('command')
pyautogui.press('l')
pyautogui.keyUp('command')

# Type the URL and press Enter
pyautogui.typewrite('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
pyautogui.press('enter')

# Delay for the page to load
time.sleep(2)

