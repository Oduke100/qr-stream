# this is the interraction point of the "fronted" and the helper functions
# ==== imports ####

from misc.data_handlers import read_data, reversal, shift, inverter
from misc.polynomial_generator import polynomial_generation
from misc.converter import convert
from misc.logic import XOR

def checksum(data):
    """
    we need to chunk the data to match the polynomial length
    actually not chunk, slice

    I have decided to name the data states with the number state it is at, with 1 being just read and the number being the degrees of manipulation
    """

    # generate the polynomial to be used first
    polynomial = polynomial_generation()

    # deal with the data
    data_state_1 = read_data(data)        # determines type of data, if str or otherwise 
    data_state_2 = convert(data_state_1)  # converts data to binary and returns a string of bits 
    
    # data reversal
    data_state_3 = ""
    for i in range(0, len(data_state_2), 8):
        group = data_state_2[i:i+8]
        data_state_3 += reversal(group)
    
    # data shifting
    data_state_4 = shift(data_state_3, 32)

    # flipping of the data
    data = data_state_4[:32]
    data_state_5 = XOR(data, ("1" * 32))

    data_state_6 = data_state_5 + data_state_4[32:]
    
    chunk = data_state_6[:len(polynomial)]
    left_over = data_state_6[len(polynomial):]
    
    for l in left_over:
        
        if chunk[0] == "1":
            chunk = XOR(chunk, polynomial)

        chunk = chunk[1:] + l

    # a divider for the last chunk
    if chunk[0] == "1":
        chunk = XOR(chunk, polynomial)

    chunk_state_2 = chunk[1:]

    chunk_state_3 = reversal(chunk_state_2)

    checksum = inverter(chunk_state_3)
    
    return checksum
