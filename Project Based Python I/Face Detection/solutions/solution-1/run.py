# Source Code Link:
# https://thecleverprogrammer.com/2020/10/09/face-detection-with-python/

import cv2

def face_detection(input_img, output_img):

    face_cascade = cv2.CascadeClassifier('data/face_detector.xml')
    img = cv2.imread(input_img)
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    
    for (x, y, w, h) in faces: 
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imwrite(output_img, img) 
    
    print('Successfully saved')

if __name__ == '__main__':
    face_detection('data/image1.png', 'output/face_detected1.png')