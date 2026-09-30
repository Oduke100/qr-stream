# the other smaller funcs that deal with the data are housed here

# ==== imports ====

import tkinter as tk
from misc.logic import XOR
from tkinter import filedialog

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
        working_data = data.encode("utf-8")
        return working_data
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
