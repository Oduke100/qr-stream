import os
import qrcode
import tkinter
from chunker import chunk_text, chunk_binary
from tkinter import filedialog

#text=input("enter your text here: ")
#file_name=input("enter the name of the qr code file you want to create: ")

def make(chunks):

	for c in range(0, len(chunks)):

		code=qrcode.make(chunks[c])
		#the .save attribute needs a file name not just a path to the folder, and I have done this more than once, prolly I will learn now that I have
		#jotted it down
		path=os.path.expanduser(f"~/sandbox/qr-stream/assets/chunk_{c}.png")
		code.save(path)

		print(f"QR code saved successfully to {path}")

chunks=chunk_binary()
code=make(chunks)
