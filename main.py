import numpy as np
import matplotlib.pyplot as plt
import cv2
from pdf2image import convert_from_path

images = list(map(np.array, convert_from_path("/Users/azsarki/Documents/books/strategy2.pdf")))
idx = 0
for image in images[0:30]:
	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	edged = cv2.Canny(image, 50, 250)
	(cnts, hierarchy) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	
	for i, c in enumerate(cnts):
		if hierarchy[0, i, 3] != -1:
			continue
		x,y,w,h = cv2.boundingRect(c)
		if w>200 and h>200:
			idx+=1
			new_img=image[y:y+h,x:x+w]
			cv2.imwrite('imgs/' + str(idx) + '.png', new_img)