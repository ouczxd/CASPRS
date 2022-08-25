#Install pyhon, numpy, scikit_image, opencv-python,and imagecodecs-lite
#Coyy the program to your image folder, and run it.
#The new images will be saved in a "8bits" sub-folder, and the image name will be saved in the TIFname.csv
import os.path
from skimage import io,img_as_float
from pathlib import Path
import cv2
import csv
import numpy as np

img_fold_A = os.path.abspath('.')
#img_fold_A.replace("\\", "/")
img_fold_B = img_fold_A+"\8bits"
print ("Source Path is ", img_fold_A)
print ("Destination Path is ", img_fold_B)
my_path = Path(img_fold_B)
if not my_path.exists():
    os.mkdir(img_fold_B)
img_list1 = os.listdir(img_fold_A)
num_imgs1 = len(img_list1)
csv_path=os.path.join(img_fold_B,'TIFname.csv')
csvFile=open(csv_path,'w',encoding='utf-8',newline="")
writer=csv.writer(csvFile)
writer.writerow(["No","Name","Min","Ratio"])
print("Image count is ", num_imgs1)

for ii in range(num_imgs1):
    name_A = img_list1[ii]    
    if name_A.endswith(".tif") or name_A.endswith(".TIF"):
        path_A = os.path.join(img_fold_A, name_A)
        im_A = io.imread(path_A)
        #im_A =im_A.astype(np.int)
        
        m1=np.percentile(im_A,2)
        m3=np.percentile(im_A,99.5)
        r=255/((m3-m1)+0.01)
        print(ii,name_A)
        writer.writerow([ii,name_A,m1,r])        
        im_A=(im_A-m1)*r
        im_A=np.minimum(im_A,255)
        im_A=np.maximum(im_A,0)        
        im_A =im_A.astype(np.uint8)
                
        file_name = os.path.join(img_fold_B, name_A)        
        io.imsave(file_name,im_A)
        
csvFile.close()
print("OK")

