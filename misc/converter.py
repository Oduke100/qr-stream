# this will be my converter file, you pass data and the type and you get back the converted form of your data

# we will start with binary conversion and improve on demand

def convert(data, width=8):
    # this converts the data to binary with a default 8 pad, unless otherwise
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
