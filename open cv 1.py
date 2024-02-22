import cv2
img = cv2.imread(r"C:\Users\ajaya\Downloads\download.jpg")
# Display the original image
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Gray Scale Image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
