# this is where we will have the data manipulation using the BG functions we have written

from misc.helpers import checksum, convert, read_data

class Data:
    def __init__(self, payload):
        self.payload = payload


    def chunk(self):
        # we need a func to chunk the data into sections that will be the transmitted chunks
        
    def tx(self):
        # this reads the payload and returns a binary string
        data = read_data(self.payload)

        # here we convert the data into binary for the checksum math and construction of full data for tx
        binary_data = convert(data)

        
        data_checksum = checksum(data)

        tx_data = binary_data + data_checksum

        print(tx_data)

mike=Data("Mike")
mike.checksum()
