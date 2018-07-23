"""
Haar-cascade Face Detection
---------------------------
Author: Jansen Penido <jansen.penido@gmail.com>
"""

# Import libraries.
import numpy as np
import cv2


def detect_faces(haar_cascade_xml):

    # Get video capture feature from default camera.
    video = cv2.VideoCapture(0)

    # Load Haar-cascade classifier.
    face_cascade = cv2.CascadeClassifier(haar_cascade_xml)

    while(True):
        # Capture image from video frame.
        ret, frame = video.read()

        # Convert image to gray to allow the detection.
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect the faces from the grey-converted image.
        faces = face_cascade.detectMultiScale(gray_frame, 1.2, 5)

        for(x,y,w,h) in faces:
            # Draw a blue rectangle on each face detected.
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

        # Display image
        cv2.imshow('frame', frame)

        # Interrump video feed when [Q] is pressed on the keyboard.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Interrump camera feed and close.
    cap.release()
    cv2.destroyAllWindows()
