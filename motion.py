import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture('http://192.168.0.100:4747/video')
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

def motion():
    count=0
    while True:
    # Read the frame
        _, img = cap.read()
    # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            if w:
                cap.release()
                return True
        count+=1
        if count==100:
            return False
# Release the VideoCapture object

