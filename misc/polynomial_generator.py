# this is where we compute the polynomial

from misc.converter import convert

# the default polynomial we use, industry standard

polynomial_hex = "04C11DB7"

def polynomial_generation():
    ref_string = "0123456789ABCDEF"
    polynomial = ""

    
    for i in polynomial_hex:
        pos = ref_string.index(i)
        binary = convert([pos], 4)

        polynomial +=  binary

    polynomial = "1" + polynomial
    return polynomial      # returns the polynomial we use in checksum

