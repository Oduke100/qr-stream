# this is where all the helper functions will reside as we create the project fresh
# the default polynomial we use, industry standard

polynomial_hex = "04C11DB7"

# we start with the most basic, a binary converter function that will take the contents of the data and change them to binary
# as I have realised, this I will have to borrow from V1 as it used the function to deal with files

import tkinter as tk
from tkinter import filedialog

# I have decided this project to construct my own converter from scratch, I need a func to divide a number by 2, save the remainder and when its done read
# the numbers from bottom up to get the binary value. also have a padd to 8 bits for numbers that wont have 8 bits

def polynomial_generation():
    ref_string = "0123456789ABCDEF"
    polynomial = ""

    
    for i in polynomial_hex:
        pos = ref_string.index(i)
        binary = convert([pos], 4)

        polynomial +=  binary

    polynomial = "1" + polynomial
    return polynomial

def convert(data, width=8):
    bite_string = ""
    
    for char in data:
        bits = []
        
        while char:
            quotient = char // 2 # (//) is the divider for whole numbers, it returns the full divider so like 13//2 gives 6
            bit = char % 2 # (%) as we know that is the modulo divider, no more explanation needed
            char = quotient
            bits.append(bit)

        # padding
        while len(bits) < width:
            bits.append(0)

        binary = "".join(str(bits[b]) for b in range(len(bits)-1, -1, -1))
        bite_string += binary
    
    return bite_string

def XOR(byte_a, byte_b):
    # just learnt sth crazy today, XOR just compares if two values are same and returns a yes or a no, 0 XOR 1 is 0(No) and 0 XOR 0 is 1 (yes)

    if len(byte_a) == len(byte_b):
        byte_values = []
        bit = 0

        for x, y in zip(byte_a, byte_b):
            if x == y:
                bit = 0
                byte_values.append(bit)
            else:
                bit = 1
                byte_values.append(bit)

        byte = "".join(str(byte_values[b]) for b in range(0, len(byte_values), 1))
        return byte
    else:
        raise ValueError("The bytes entered are NOT of the same length!")

def shift(data, places):

    if places >= 0:
        for p in range(places):
            result = data + "0"
            data = result

        return data
    else:
        raise ValueError("The number of places shifted cannot be less than 0")
    
def read_file():
    root = tk.Tk()

    root.withdraw()
    filepath=filedialog.askopenfilename()

    file = open(filepath, "rb") # this is just the init connection to the file, we need to read what is in the file, thus

    data=file.read()
    file.close()

    return data

def read_data(data):
    if isinstance(data, str):
        working_data = data.encode("utf-8")
        return working_data
    else:
        return data

def reversal(data):
    reversed_string = "".join(str(data[i]) for i in range(len(data)-1, -1, -1))
    return reversed_string

def inverter(data):
    inverted_string = XOR(data, ("1" * len(data)))

    return inverted_string

def checksum(data):
    # we need to chunk the data to match the polynomial length
    # actually not chunk, slice

    working_data = read_data(data)
    
    data_4_use = convert(working_data)
    polynomial = polynomial_generation()

    # data reversal
    reversed_data = ""
    for i in range(0, len(data_4_use), 8):
        group = data_4_use[i:i+8]
        reversed_data += reversal(group)
    
    # data shifting
    shifted_data = shift(reversed_data, 32)

    # flipping of the data
    data = shifted_data[:32]
    flipped_data = XOR(data, ("1" * 32))

    data_2b_used = flipped_data + shifted_data[32:]
    
    chunk = data_2b_used[:len(polynomial)]
    left_over = data_2b_used[len(polynomial):]
    
    for l in left_over:
        
        if chunk[0] == "1":
            chunk = XOR(chunk, polynomial)

        chunk = chunk[1:] + l

    # a divider for the last chunk
    if chunk[0] == "1":
        chunk = XOR(chunk, polynomial)

    working_chunk = chunk[1:]

    final_chunk = reversal(working_chunk)

    data_output = inverter(final_chunk)
    
    return data_output
    
# test=checksum([1, 2, 3])
test=checksum("Hello")
print(test)
# polynomial= polynomial_generation()
# print(polynomial)
