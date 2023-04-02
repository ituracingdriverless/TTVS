import cv2
import os

# Path to directory containing images and labels
dir_path = "./"

# Load class names from classes.txt file
with open(os.path.join(dir_path, "classes.txt")) as f:
    classes = [line.strip() for line in f.readlines()]

# Loop through each PNG image file in the directory
label_count = 0
classes_count = [0 for i in range(len(classes))]
for filename in os.listdir(dir_path):
    if filename.endswith(".png"):
        # Load image using OpenCV
        img = cv2.imread(os.path.join(dir_path, filename))

        # Load YOLO format label from corresponding text file
        label_file = os.path.join(dir_path, os.path.splitext(filename)[0] + ".txt")
        try:
            with open(label_file) as f:
                lines = f.readlines()
        except:
            continue
        labels = []
        for line in lines:
            parts = line.strip().split()
            class_idx = int(parts[0])
            x, y, w, h = [float(part) for part in parts[1:]]
            labels.append((class_idx, x, y, w, h))
        
        # Display image and labels
        for label in labels:
            class_idx, x, y, w, h = label
            class_name = classes[class_idx]
            left = int((x - w/2) * img.shape[1])
            top = int((y - h/2) * img.shape[0])
            right = int((x + w/2) * img.shape[1])
            bottom = int((y + h/2) * img.shape[0])
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(img, class_name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            classes_count[class_idx] += 1
            label_count += 1
            

        cv2.imshow("photo", cv2.resize(img, (int(img.shape[1]/(1.5)), int(img.shape[0]/1.5))))
        cv2.waitKey(0)
        #cv2.destroyAllWindows()
