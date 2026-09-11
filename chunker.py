import tkinter as tk
from tkinter import filedialog

def chunk_text(text):
	chunks=[]
	size=10

	for i in range(0, len(text), size):
		chunk=text[i:i+size]
		chunks.append(chunk)

	print(chunks)

def chunk_binary():

	root=tk.Tk()
	root.withdraw()

	filepath=filedialog.askopenfilename()

	file=open(filepath, "rb")
	chunks=[]
	size=35

	chunk=file.read(size)

	while chunk:
		chunks.append(chunk)
		chunk=file.read(size)

	file.close()
	return chunks
