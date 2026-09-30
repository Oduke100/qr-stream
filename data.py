# this is where we will have the data manipulation using the BG functions we have written

from misc.data_handlers import read_data
from misc.converter import convert
from misc.checksum import checksum

"""
we need to create a matrix class, this will hold;
1, the most important, the matrix
2, the order ie x/total - probably in binary
3, the data, after chunking as the data will most definately be large

"""

class Data:
    def __init__(self, payload):
        self.payload = payload

    def tx(self):
        data_state_1 = read_data(self.payload)

        data_state_2 = convert(data_state_1)     # this converts the whole raw data to binary
        data_state_3 = checksum(data_state_1)

        data_state_4 = data_state_2 + data_state_3

        print(len(data_state_4))
        
mike=Data("Mike")
mike.tx()
