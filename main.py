import time
import ctypes
import keyboard
from threading import Thread

# Constants for mouse events
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_ABSOLUTE = 0x8000

# Flag to stop
stop_flag = False

# Move the cursor to the specified coordinates
ctypes.windll.user32.SetCursorPos(1318, 449)


# Function for tracking 'Q' key presses
def check_stop():
    global stop_flag
    keyboard.wait('q')  # Waiting for 'Q' to be pressed
    stop_flag = True
    print('The "Q" key is pressed. Stop.')


# Function for click emulation
def click():
    # Move the cursor to the specified coordinates
    # ctypes.windll.user32.SetCursorPos(x, y)q
    # Emulate pressing and releasing the left mouse button
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.03)  # Short delay

    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# Main function
def main():
    time.sleep(3)  # Delay before starting
    print('Launch!\nPress "Q" to stop.')

    # Start a thread to track 'Q' key presses
    stop_thread = Thread(target=check_stop)
    # Demonize the thread so that it ends with the main thread
    stop_thread.daemon = True
    stop_thread.start()

    # Main cycle for clicks
    while True:
        if stop_flag:  # Checking the stop flag
            break
        click()  # Click on coordinates (1318, 449)
        time.sleep(0.01)  # Delay between clicks (in seconds)

    print('Done!')


if __name__ == "__main__":
    main()
