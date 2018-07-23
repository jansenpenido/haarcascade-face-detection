"""
Haar-cascade Face Detection
---------------------------
Author: Jansen Penido <jansen.penido@gmail.com>
"""

from src import face_detection as fd

# Haar-cascade XML file path.
HAAR_CASCADE_XML = 'cascade/haarcascade_frontalface_default.xml'

# Detect faces from the camera feed.
fd.detect_faces(HAAR_CASCADE_XML)
