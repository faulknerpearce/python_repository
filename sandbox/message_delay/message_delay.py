import time
import sys

player = 'Austin'
text = f"\nHello {player} welcome to the Gladiators game."

def delayed_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    # Add a newline character at the end of the text
    sys.stdout.write('\n')
    sys.stdout.flush()

#delayed_print(text)

def delayed_input(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    
    return input()

delayed_print(text, 0.5)