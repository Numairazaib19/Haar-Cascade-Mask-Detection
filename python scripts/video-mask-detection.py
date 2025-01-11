import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load the custom Haar Cascade for mask detection
mask_cascade = cv2.CascadeClassifier('./myhaar.xml')

# Open the video file (replace 'video.mp4' with your video file path)
cap = cv2.VideoCapture('videos/video1.mp4')

# Check if the video file is opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Set up the figure and axis for matplotlib
fig, ax = plt.subplots()

# Read the first frame
ret, frame = cap.read()
if not ret:
    print("Error reading the video")
    exit()

# Initial display of the first frame
im = ax.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
ax.axis('off')  # Turn off the axis for a cleaner view

# Function to update each frame in the plot
def update_frame(i):
    ret, frame = cap.read()
    if not ret:
        return im  # Return the same frame if the video has ended

    # Convert the frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect masks
    masks = mask_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    # Draw rectangles around detected masks
    for (x, y, w, h) in masks:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue rectangle for mask

    # Update the plot with the new frame
    im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    return im

# Create an animation to run the video
ani = animation.FuncAnimation(fig, update_frame, interval=30)

plt.show()

# Release the video capture object when done
cap.release()
