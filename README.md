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

Importing in Your Code:

<li>In your Python script, import the OpenCV module:</li>
import cv2

<li>Usage:</li>

Use OpenCV functions for tasks like image manipulation, object detection, face recognition, and more.
Refer to the official OpenCV documentation for detailed information on available functions and usage examples.
</ol>

<h2>3. Purpose of the Program</h2>
<p>The purpose of this program is to demonstrate how to install and use OpenCV in Python. It provides a starting point for developers who want to explore computer vision applications.</p>

<h2>4. Sample Input/Output</h2>
<h3>Input:</h3> <p>An image or video file.</p>
<h3>Output:</h3> <p>Processed images with applied filters, contours, or other transformations.</p>
For example:

<pre><code>import cv2

# Read an image from file
image = cv2.imread('sample_image.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray_image, 100, 200)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()</code></pre>

Remember to replace 'sample_image.jpg' with the actual path to your image file.