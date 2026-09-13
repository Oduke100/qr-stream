import os
import qrcode
import tkinter
from chunker import chunk_text, chunk_binary
from tkinter import filedialog

#text=input("enter your text here: ")
#file_name=input("enter the name of the qr code file you want to create: ")

def make(chunks):
# this function is what creates the QR codes for the data we get from chunks.

	for c in range(0, len(chunks)): # same explanation as in chunks, start from x to y with the size of size.

		code=qrcode.make(chunks[c]) # this is the actual QR code building block

		#the .save attribute needs a file name not just a path to the folder, and I have done this more than once, prolly I will learn now that I have
		#jotted it down

		path=os.path.expanduser(f"~/sandbox/qr-stream/assets/chunk_{c}.png")
		code.save(path)

		print(f"QR code saved successfully to {path}")

chunks=chunk_binary()
code=make(chunks)
