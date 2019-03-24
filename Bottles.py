import win10toast
import time
import datetime
import sys
import os
from infi.systray import SysTrayIcon


class BottlesNotifier(win10toast.ToastNotifier):
    # TODO: allow for customizable durations (semi-obvious)
    def __init__(self):
        super()  # using super() for inheritance
        self.duration = 20
        self.icon_special = resource_path("data/bottles.ico")


    @staticmethod
    def time_string():
        time_string = datetime.datetime.now().strftime("%I:%M:%S %p")
        return "Bottles - " + time_string

    @staticmethod
    def water_string(duration):
        if duration == 1:
            return "It's been a minute. DRINK."
        else:
            return "It's been " + str(duration) + " minutes, drink some water! Refill that water bottle!"

    @staticmethod
    def simple_wait(duration):
        minutes = 0
        while minutes != duration:
            time.sleep(60)
            minutes += 1

    def bottles_cycle(self):
        """
        Performs a wait cycle and then dispatches a notification
        """
        self.simple_wait(self.duration)
        self.show_toast(self.time_string(),
                        self.water_string(self.duration),
                        icon_path=self.icon_special,
                        duration=5)


class BottlesTray(object):
    def __init__(self):
        self.icon_special = resource_path("data/bottles.ico")
        self.notifier = BottlesNotifier()
        self.notifier.show_toast(self.notifier.time_string(),
                        "Bottles will start reminding you to drink every 20 minutes.",
                        icon_path=self.icon_special,
                        duration=5)
        self.menu_options = (("About", None, self.skip),)
        self.tray = SysTrayIcon(self.icon_special, "Bottles", on_quit=bye)

    @staticmethod
    def skip():
        pass

    def start_alarm(self):
        self.notifier.bottles_cycle()

def bye(sysTrayIcon):
    sys.exit()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

