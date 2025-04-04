import pyautogui
import time
from reader import select_reader, wait_and_read_uid, formated_uid

reader = select_reader()

def main():

    print("Badge emulator running. Waiting for cards...")

    while True:
        uid_array = wait_and_read_uid(reader)

        if uid_array:
            uid_string = formated_uid(uid_array)
            pyautogui.write(uid_string)
            pyautogui.press("enter")
            print(f"UID detected and typed: {uid_string}")
            time.sleep(5)

        time.sleep(0.2)


if __name__ == "__main__":
    main()
