import os
import cv2

filepath=os.path.expanduser("~/sandbox/qr-stream/assets")

def streamer(filepath):
#this is the function that will initiate the stream, it pops a window and shows the codes.
#this function still needs a sequencer, thats what will ensure the codes are displayed in order of each other

	filenames=os.listdir(filepath)
	for f in filenames:
		#this is the path builder
		path=filepath+f"/{f}"

		image=cv2.imread(path)

		cv2.imshow("QR stream", image)
		cv2.waitKey(33)


	cv2.destroyAllWindows()

filenames=streamer(filepath)
