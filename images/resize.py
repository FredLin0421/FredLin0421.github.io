import cv2

img = cv2.imread('haptic.png')
reimg = cv2.resize(img,(300,300))

cv2.imwrite('haptic_re.png',reimg)
cv2.imshow("Resized image", reimg)
cv2.waitKey(0)
cv2.destroyAllWindows()