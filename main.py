import os
import qrcode

text=input("enter your text here: ")

def test(text):
	code=qrcode.make(text)
	#the .save attribute needs a file name not just a path to the folder, and I have done this more than once, prolly I will learn now that I have
	#jotted it down
	path=os.path.expanduser("~/sandbox/qr-stream/assets/test.png")
	code.save(path)

	print(f"QR code saved successfully to {path}")
	return code

code=test(text)
