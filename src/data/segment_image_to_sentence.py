from settings import FILE_DATA_EXEMPLE, DIR_DATA_LINES_KHALIL
import cv2
import numpy as np
import image
import os

img = cv2.imread(FILE_DATA_EXEMPLE)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5,100), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)

im2, ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)

    # Getting ROI
    roi = img[y:y+h, x:x+w]

    # show ROI
    path_name = os.path.join(DIR_DATA_LINES_KHALIL, 'segment_no_'+str(i)+'_expl.jpg')
    print(path_name)
    cv2.imwrite(path_name, roi)
