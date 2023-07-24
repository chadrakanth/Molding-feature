import cv2
import numpy as np
import os


# Load the images
img1 = cv2.imread('/home/ssg/Desktop/project/Molding-feature/templates/0.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('image2.jpg', cv2.IMREAD_GRAYSCALE)

# Create SURF object
surf = cv2.xfeatures2d.SURF_create()

# Detect keypoints and compute descriptors for both images
kp1, des1 = surf.detectAndCompute(img1, None)
kp2, des2 = surf.detectAndCompute(img2, None)

# Create a brute-force matcher object
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

# Match the descriptors
matches = bf.match(des1, des2)

# Sort the matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw the top 10 matches
result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

# Display the result
cv2.imshow('SURF Matches', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
