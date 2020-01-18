import numpy as np
import cv2
from PIL import Image
import pytesseract
 

input_link = 'C:\\Users\\karti\\OneDrive\\Desktop\\cvision\\input images\\txt_mudit_b8_'

#str(i)  i = 1,2,3.................acording to the image
img = cv2.imread(input_link + str(1) +'.jpg')
 
img2 = img.reshape((-1,3))
 
img2 = np.float32(img2)
    
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename), lang='fra')   
    return text

# k will be decided according to the image for clustering

k=2
attempts =10
    
ret,label,center=cv2.kmeans(img2,k,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
    
center = np.uint8(center)
    
res = center[label.flatten()]
res2 = res.reshape(img.shape)

cv2.imwrite('C:\\Users\\karti\\OneDrive\\Desktop\\cvision\\Segmented Images\\'+'segmented'+str(1)+'.jpg',res2)

text_e = ocr_core('C:\\Users\\karti\\OneDrive\\Desktop\\cvision\\Segmented Images\\'+'segmented'+str(1)+'.jpg')
