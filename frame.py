"""
this is the HQ for the frame engineering where we will pass the data and stream

this is the formula I used to get the number of frames;

frames = total bytes ÷ bytes per frame

now this is the analogy I used,
the string "Mike" assuming its a binary, the letter "M" is the byte and this byte is composed of 8 bits in it, so "Mike" is made of 32 bits

now our Orientation system takes up 8 bits
then the frame count takes up 21 bits(*2) this is because we need to count as x/total and total is 21 bits long meaning the x can also onlt be 21 bits long
then the 16 checksum(we will truncate the 32 bit checksum we calculate to just 16)

all this sums up to:
8 + 58 gives 66

and we have a 29*29 grid to play with which gives 841 bits and we already have budgetted for 66 of those
this leaves 775, but 96 bytes gives 768 bytes so we went with 96 full bytes and 7 extra bits

so the data portion will be 96 bytes per frame

with this data we can confidently chunk the data as we know what size we are chunking it to
"""

from misc.frame import frame_data

mike = frame_data("The quick brown fox jumps over the lazy dog while the sun sets slowly behind the hills, painting the sky in shades of orange and pink. Birds return to their nests, the river hums a quiet tune, and somewhere far away a lone train whistles into the night.")
print(mike)
print(len(mike))
