# Returns 1 if both inputs are 1, otherwise returns 0.
def AND_gate(a, b):
    if a and b:
        return 1
    return 0

# Returns 1 if the input is 0, otherwise returns 0.
def NOT_gate(a):
    if a:
        return 0
    return 1

# Returns 1 if at least one input is 1, otherwise returns 0.
def OR_gate(a, b):
    if a or b:
        return 1
    return 0

# Returns 0 if both inputs are 1, otherwise returns 1.
def NAND_gate(a, b):
    return 0 if a and b else 1

# Returns 1 if the inputs are different, otherwise returns 0.
def XOR_gate(a, b):
    return 1 if (a and not b) or (not a and b) else 0