import os
import qrcode

text="0"

def test():

	code=qrcode.make(text)
	path=os.path.expanduser("~/sandbox/qr-stream/assets/test.png")
	code.save(path)

	return {"message": "saved successfully"}

code=test()
