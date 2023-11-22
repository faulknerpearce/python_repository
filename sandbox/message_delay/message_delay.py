import time
import sys

user = 'James'
test_text = f"\nHello {user}, this is an output test."

def delayed_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    # Add a newline character at the end of the text
    sys.stdout.write('\n')
    sys.stdout.flush()

#delayed_print(text)


# Will slowly print an input message to the terminal. 
def delayed_input(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    
    return input()

delayed_print(test_text, 0.5)