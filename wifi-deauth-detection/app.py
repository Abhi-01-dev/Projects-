import threading
from detector import start_detection
from gui import start_gui

if __name__ == "__main__":
    detector_thread = threading.Thread(target=start_detection, daemon=True)
    detector_thread.start()

    start_gui()
