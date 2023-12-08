import time
import sys

def delayed_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    # Add a newline character at the end of the text
    sys.stdout.write('\n')
    sys.stdout.flush()

def delayed_input(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    
    return input()