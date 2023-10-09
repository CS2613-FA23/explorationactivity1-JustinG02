[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oB7VDeFN)
# ExplorationActivity1 - OpenCV Python Package

<h2>1. Package/Library Demonstrated</h2>
<p>The sample program showcases the usage of the OpenCV library for Python. OpenCV (Open Source Computer Vision Library) is a powerful open-source library for computer vision, image processing, and machine learning tasks.<p>

<h2>2. Running the Program</h2>
<p>To use OpenCV in your Python project, follow these steps:</p>

<h3>Installation:</h3>

<ol>
<li>Install OpenCV using pip:</li>
<pre><code>pip install opencv-python</code></pre>

<h3>Importing in Your Code:</h3>

<li>In your Python script, import the OpenCV module:</li>
<pre><code>import cv2</code><pre>

<li>Usage:</li>

Use OpenCV functions for tasks like image manipulation, object detection, face recognition, and more.
Refer to the official OpenCV documentation for detailed information on available functions and usage examples. [OpenCV Official Documentation](https://docs.opencv.org/)
</ol>

<h2>3. Purpose of the Program</h2>
<p>The purpose of this program is to demonstrate how to install and use OpenCV in Python. It provides a starting point for developers who want to explore computer vision applications.</p>

<h2>4. Sample Input/Output</h2>
<h3>Input:</h3> <p>An image file.</p>
<h3>Output:</h3> <p>Processed image with blur applied to detected faces.</p>
For example:

<pre><code>import numpy as np 
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
plotImages(image)</code></pre>

Remember to replace 'sample_image.jpg' with the actual path to your image file.