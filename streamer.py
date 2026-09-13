import os
import cv2

filepath=os.path.expanduser("~/sandbox/qr-stream/assets")

def streamer(filepath):

	filenames=os.listdir(filepath)
	for f in filenames:
		path=filepath+f"/{f}"

		image=cv2.imread(path)
		cv2.imshow("QR stream", image)
		cv2.waitKey(33)


	cv2.destroyAllWindows()

filenames=streamer(filepath)
