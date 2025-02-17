# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "opencv-python-headless",
#     "matplotlib",
# ]
# ///

import cv2

# Get user inputs
video_path = input("Enter path to video file: ")
output_path = input("Enter output image path: ")
new_width = int(input("Enter desired width: "))
new_height = int(input("Enter desired height: "))

# Read video and get first frame
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video file")
    exit()

ret, frame = cap.read()
if not ret:
    print("Error: Could not read first frame")
    exit()

# Resize the frame
resized_frame = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_AREA)

# Save the resized frame
cv2.imwrite(output_path, resized_frame)
print(f"Successfully saved resized frame to {output_path}")

