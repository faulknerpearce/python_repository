from gates import AND_gate, OR_gate, XOR_gate

# Implements a half-adder using XOR and AND gates to calculate the sum and carry-out of two bits.
def half_adder(a, b):
    s = XOR_gate(a, b)
    c = AND_gate(a, b)
    return s, c

# Implements a full-adder using two half-adders and an OR gate to calculate the sum and carry-out of three bits.
def full_adder(a, b, c):
    s1, c1 = half_adder(a, b)
    s, c2 = half_adder(s1, c)
    c_out = OR_gate(c1, c2)
    return (s, c_out)

# Implements an Arithmetic Logic Unit (ALU) to perform addition operations based on an opcode.
# If opcode is true, performs full addition of three bits; otherwise, performs half addition of two bits.
def ALU(a, b, c, opcode):
    if opcode:
        s, c = full_adder(a, b, c)
    else:
        s, c = half_adder(a, b)
    return s, c

print(half_adder(1, 1))  # Example usage to test the half_adder function.