import pyautogui
import time
from lib.smart_card_reader import SmartCardReader
from lib.keyboard_writer import KeyboardWriter

reader = SmartCardReader()
keyboard = KeyboardWriter()

def main():

    nfc_reader = None

    while not nfc_reader:
        print("Looking for a NFC reader...")
        nfc_reader = reader.select_reader()
        if not nfc_reader:
            time.sleep(5)


    print("Badge emulator running. Waiting for cards...")

    while True:
        uid = reader.read_uid()

        if uid:
            keyboard.write_uid(uid)
            keyboard.press_enter()
            print(f"UID detected and typed: {uid}")
            time.sleep(5)

        time.sleep(0.2)


if __name__ == "__main__":
    main()