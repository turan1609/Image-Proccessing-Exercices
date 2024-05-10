import cv2

# Load the images
img1 = cv2.imread("substrack1.jpg")
img2 = cv2.imread("substrack2.jpg")

# Convert images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Compute absolute difference between the two grayscale images
diff = cv2.absdiff(gray1, gray2)

# Threshold the difference image
_, thresholded_diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

# Show the difference image and the original images
cv2.imshow("Difference Image", thresholded_diff)
cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
