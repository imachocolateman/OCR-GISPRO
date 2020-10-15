import cv2
import numpy as np

img = cv2.imread('/Users/sanchitkumar/OneDrive - IGO Limited/General Tasks/Pdf_to_text/Images/CR1996-0011 Sons of Gwalia Edwards and Kellow 1996-single.png', cv2.IMREAD_GRAYSCALE)
inverted = cv2.bitwise_not(img)

kernel = np.ones((2, 2), np.uint8)
erosion = cv2.erode(inverted, kernel, iterations=1)

inverted = cv2.bitwise_not(erosion)

cv2.imshow('Image', inverted)
cv2.waitKey(0)
cv2.destroyAllWindows()
