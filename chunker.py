import tkinter as tk
from tkinter import filedialog

def chunk_text(text):
#this will chunk texts for transfer, its a test function and likely wont be used in prod

	chunks=[]
	size=10

#for loops are actually interesting, in this case, this function reads as: for any 1 instance(where the condition is matched) between 0(starting point) and
#[len(text) ending point] with a chunk size of size(this is normally not passed but the function allows). It's actually soo cool coz its a bit complex at
#time of writting

	for i in range(0, len(text), size):
		chunk=text[i:i+size]
		#same as a note I did on my last project, append takes the list name.
		chunks.append(chunk)

	print(chunks)

def chunk_binary():
#now this function is like prolly the brain of the whole project as its what we will use in transfer of the big files(mnedia and so on)
#it reads the file(asks user to pick a file from storage(I am thinking of adding a capability to pass the file path), it reads the file in binary(the "rb"
#in  open(filepath, "rb") literally means read-binary. then it chunks the binary normally like the chunk_text() function and returns the chunks list


	root=tk.Tk() # This is a crucial step in the tkinter library I am using as it has to have a pre-screen before it opens dialog(this opens it and closes
		#it immediately

	root.withdraw()

	filepath=filedialog.askopenfilename()

	file=open(filepath, "rb")
	chunks=[]
	size=35

	chunk=file.read(size) #this reads file size to give the while loop a starting point


#now here a while loop is used since, binary can return a 0 and that is our signal so the while loop is so that we are not locked in an infinite loop
#since if we used for it'd append even the 0s

	while chunk:
		chunks.append(chunk)
		chunk=file.read(size) # this reads the file to continue the while loop

	file.close() #self explanatory

	return chunks
