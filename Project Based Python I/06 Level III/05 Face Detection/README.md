<img src="./images/face-detection.png" width="700"/>

# Face Detection
> DIFFICULTY: **INTERMEDIATE**

Face detection is the process of detecting faces from an image. Use **OpenCV** library in Python which is used as the primary tool for the tasks of computer vision in Python. You need to install the OpenCV library in Python

OpenCV library in python is blessed with many pre-trained classifiers for face, eyes, smile, etc. These XML files are stored in a folder. We use the face detection model. (xml file is in data folder)


## TODO

1. Use cv2 to laod 'face_detector.xml' in data directory.
2. Use cv2 to read input image.
3. Detect the faces in input image.
4. Draw a rectangle around each faces in the input image.
5. Store the output image in output directory.

## How to Run

- Install the requirements by running pip install -r requirements.txt.
- Chagne 'data/image1.png' with your image path in following line (last line of code):
```python
face_detection('data/image1.png', "output/face_detected1.png")
```
- Run **python run.py** to start face detection.