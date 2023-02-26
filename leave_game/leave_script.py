import pyautogui
import time


def leave_game(delay):
    time.sleep(delay)

    # Press the Esc key
    pyautogui.press('esc')
    time.sleep(delay)

    # Press the End key
    pyautogui.press('end')
    time.sleep(delay)

    # Press the Enter key
    pyautogui.press('enter')
    time.sleep(delay)

    # Press the Home key
    pyautogui.press('up')
    time.sleep(delay)

    # Press the Enter key
    pyautogui.press('enter')
    time.sleep(delay)

    # OPTIONAL - Enter in the game again
    # This could variates the time your game takes to load the title screen
    # time.sleep(load_title_screen_time)
    # pyautogui.press('enter')
