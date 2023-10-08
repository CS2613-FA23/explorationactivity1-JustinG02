import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
  
# Plots given image
def plotImages(img): 
    plt.imshow(img, cmap="gray") 
    plt.axis('off') 
    plt.style.use('seaborn-v0_8') 
    plt.show() 

# Read image
image = cv2.imread('my_img.jpg') 
  
# Convert image from BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

# Detects faces using classifier found at https://www.geeksforgeeks.org/face-detection-using-cascade-classifier-using-opencv-python/
face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
face_data = face_detect.detectMultiScale(image, 1.3, 5) 
  
# Draws region around face 
for (x, y, w, h) in face_data: 
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) 
    face = image[y:y+h, x:x+w] 
    # Apply blur over region
    face = cv2.GaussianBlur(face, (23, 23), 30) 
    image[y:y+face.shape[0], x:x+face.shape[1]] = face 
  
  
# Display final image
plotImages(image)