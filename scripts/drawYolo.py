from os import listdir
from os.path import isfile,join
import cv2

path = '/home/limon/workspace/datasets/trafficLabels/'
Read_path = path + 'yoloLabels/'
img_path = path + 'images/'

for f in listdir(Read_path):
	if isfile(join(Read_path, f)):
		name,ext = f.split('.')
		img = cv2.imread(img_path + name + '.jpg')
		h,w,_ = img.shape
		print(img_path+name)
		print(h,w)
		f = open(Read_path+f, "r")
		lines = f.readlines()

		for line in lines:
			data = line.split(" ")

			obj = data[0]
			bbox_width = float(data[3]) * w
			bbox_height = float(data[4]) * h
			center_x = float(data[1]) * w
			center_y = float(data[2]) * h
			top_left = (int(center_x - bbox_width/2),int(center_y	- bbox_height/2))
			bottom_right = (int(center_x + bbox_width/2),int(center_y + bbox_height/2))
			print(obj)
			cv2.rectangle(img,top_left,bottom_right,(0,255,0),3) #human


		f.close()
		cv2.imshow('image',img)
		k = cv2.waitKey(0)
		if k == 27:         # wait for ESC key to exit
		    exit()
		elif k == ord('s'):
			cv2.destroyAllWindows()