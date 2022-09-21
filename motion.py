import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from IP Camera
cap = cv2.VideoCapture('http://192.168.0.100:4747/video')


def motion():
    count=0
    while True:
    # Reads the frame
        _, img = cap.read()
    # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            if w:
                cap.release() # Release the video capure object
                return True   #Returns true when a face is detected
        count+=1
        if count==100:
            return False

