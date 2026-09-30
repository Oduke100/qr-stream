# this will house all my logic gates, all that I use in this proj.

def XOR(byte_a, byte_b):
    # just learnt sth crazy today, XOR just compares if two values are same and returns a yes or a no, 0 XOR 1 is 0(No) and 0 XOR 0 is 1 (yes)

    if len(byte_a) == len(byte_b):
        bit_values = []
        bit = 0

        for x, y in zip(byte_a, byte_b):
            if x == y:
                bit = 0
                bit_values.append(bit)
            else:
                bit = 1
                bit_values.append(bit)

        byte = "".join(str(bit_values[b]) for b in range(0, len(bit_values), 1))
        return byte
    else:
        raise ValueError("The bytes entered are NOT of the same length!")
