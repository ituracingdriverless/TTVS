from os import listdir
from os.path import isfile,join
import cv2

path = '/home/limon/workspace/datasets/trafficLabels/'
label_path = path + 'labels/'
image_path = path + 'images/'
Write_path = path + 'yoloLabels/'

etiket = {
    "dur":"0",
    "durak":"1", 
    "sagaDonulmez":"2",
    "solaDonulmez":"3",
    "girilmez":"4",
    "tasitGiremez":"5",
    "parkYasak":"6",
    "park":"7",
    "trafikIsigi":"8"
}

def to_yolo(path):
    file_name = path.split('.',1)
    image_full_path = image_path+file_name[0]  +".jpg"
    print(image_full_path)
    img = cv2.imread(image_full_path)
    img_height,img_width,_ = img.shape
    f = open(label_path+path, "r")
    txt = open(Write_path+path,"w")
    lines = f.readlines()

    for line in lines:
        features = line.split(",")
        x1,y1,x2,y2 = int(features[1]),int(features[2]),int(features[3]),int(features[4])
        x,y = x1,y1
        width = x2-x1
        height = y2-y1
        obj = features[0]
        obj_cls = etiket[obj]
        if obj_cls is not None:
            yolo_x = float(x + width//2)/img_width
            yolo_y = float(y + height//2)/img_height
            yolo_width = float(width)/img_width
            yolo_height = float(height)/img_height
            txt.write(obj_cls+' '+str(yolo_x)+' '+str(yolo_y)+' '+str(yolo_width)+' '+str(yolo_height)+'\n')
    
    txt.close()
    f.close()
    
    return None

for f in listdir(label_path):
    if isfile(join(label_path, f)):
        to_yolo(f)



