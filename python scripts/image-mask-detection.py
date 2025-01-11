import cv2
import matplotlib.pyplot as plt

# Load the mask detection Haar Cascade XML file
mask_cascade = cv2.CascadeClassifier('./myhaar.xml')

# Load the image where you want to detect masks
img = cv2.imread('images/pic2.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect masks in the image
masks = mask_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected masks
for (x, y, w, h) in masks:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue rectangle for mask detection

# Convert BGR to RGB for displaying using matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display using matplotlib
plt.imshow(img_rgb)
plt.axis('off')  # Hide axes
plt.show()

# Optionally, save the result to a file
cv2.imwrite('img_results/result.jpg', img)
