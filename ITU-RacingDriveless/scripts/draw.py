from os import listdir
from os.path import isfile,join
import cv2

path = '/home/limon/workspace/datasets/trafficLabels/'
Read_path = path + 'labels/'
img_path = path + 'images/'

for f in listdir(Read_path):
    if isfile(join(Read_path, f)):
        name,ext = f.split('.')
        img = cv2.imread(img_path + name + '.jpg')
        h,w,_ = img.shape
        print(name)
        f = open(Read_path+f, "r")
        lines = f.readlines()
        for line in lines:
            data = line.split(",")
            obj = data[0]
            x1 = int(data[1])
            y1 = int(data[2])
            x2 = int(data[3])
            y2 = int(data[4]) 
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3) 

        f.close()
        cv2.imshow('image',img)
        k = cv2.waitKey(0)
        if k == 27:         # wait for ESC key to exit
            exit()
        elif k == ord('s'):
            cv2.destroyAllWindows()
   
