# this is where all the helper functions will reside as we create the project fresh

# we start with the most basic, a binary converter function that will take the contents of the data and change them to binary
# as I have realised, this I will have to borrow from V1 as it used the function to deal with files

import tkinter as tk
from tkinter import filedialog

# I have decided this project to construct my own converter from scratch, I need a func to divide a number by 2, save the remainder and when its done read
# the numbers from bottom up to get the binary value. also have a padd to 8 bits for numbers that wont have 8 bits

def convert(data):
    byte_list = []
    
    for char in data:
        bits= []
        
        while char:
            quotient = char // 2 # (//) is the divider for whole numbers, it returns the full divider so like 13//2 gives 6
            bit = char % 2 # (%) as we know that is the modulo divider, no more explanation needed
            char = quotient
            bits.append(bit)

        while len(bits) < 8:
            bits.append(0)

        binary = "".join(str(bits[b]) for b in range(len(bits)-1, -1, -1))
        byte_list.append(binary)

    return byte_list

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

# def shitf(data, places):  
    
def read_file():
    root = tk.Tk()

    root.withdraw()
    filepath=filedialog.askopenfilename()

    file = open(filepath, "rb") # this is just the init connection to the file, we need to read what is in the file, thus

    data=file.read()
    file.close()

    return data

test=XOR("101", "10")
print(test)
