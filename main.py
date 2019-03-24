from Bottles import BottlesNotifier, BottlesTray

if __name__ == "__main__":
    bottles_tray = BottlesTray()
    bottles_tray.tray.start()
    bottles_tray.start_alarm()

