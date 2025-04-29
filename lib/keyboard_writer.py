import pyautogui

class KeyboardWriter:

    def write_uid(self, formatted_uid : str):
        pyautogui.write(formatted_uid)

    def press_enter(self):
        pyautogui.press("enter")
