# the other smaller funcs that deal with the data are housed here

# ==== constants ====

number_of_bytes = 96
chunk_size = (number_of_bytes * 8)

# ==== imports ====

import tkinter as tk
from misc.logic import XOR
from tkinter import filedialog
from misc.converter import convert

# ==== data readers ====

def read_file():
    root = tk.Tk()

    root.withdraw()
    filepath=filedialog.askopenfilename()

    file = open(filepath, "rb") # this is just the init connection to the file, we need to read what is in the file, thus

    data=file.read()
    file.close()

    return data       # data in binary

def read_data(data):
    if isinstance(data, str):
        data_state_1 = data.encode("utf-8")
        return data_state_1
    else:
        return data    # checks if data is str or otherwise

# ==== data manipulators ====
    
def reversal(data):
    reversed_string = "".join(str(data[i]) for i in range(len(data)-1, -1, -1))
    return reversed_string

def inverter(data):
    inverted_string = XOR(data, ("1" * len(data)))

    return inverted_string

def shift(data, places):

    if places >= 0:
        for p in range(places):
            result = data + "0"
            data = result

        return data
    else:
        raise ValueError("The number of places shifted cannot be less than 0")

# ==== data formatters ====

def chunker(data):
    data_state_1 = read_data(data)

    data_state_2 = convert(data_state_1)    # this will return our data in binary strings

    chunks = []
    chunk_sizes = []

    payload_bits = ""

    for i in range(0, len(data_state_2), chunk_size):
        payload_bits = data_state_2[i:i+chunk_size]

        # we need to pad this chunks too so they all are (96*8)bits long all the time
        chunk_length = read_data(len(payload_bits))

        chunk_length = chunk_length // 8  # this gives the bytes and not the bits
        chunk_sizes.append(chunk_length)
        
        chunk_length_state_1 = convert([chunk_length], width=7)
        
        if len(payload_bits) < chunk_size:
            payload = payload_bits + ("0" * (chunk_size - len(payload_bits)))
            chunks.append(payload)

        else:
            chunks.append(payload_bits)
            
    return chunk_sizes, chunks
