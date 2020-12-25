# Detect Cars in Video_Frame

# import python OpenCV
import cv2

# capture frames from video
cap = cv2.VideoCapture('video.avi')

# Trained XML classifiers describes some features of object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')

# loop runs if capturing is initialized
while True:
    # reads frames from video
    ret, frames = cap.read()

    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # detects cars of different sizes in input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # drawing rectangle in each cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # display frames in window
    cv2.imshow('Vehicle Detection', frames)

    # wait for ESC key to stop
    if cv2.waitKey(33) == 27:
        break
# de-allocate any associated memory usage
cv2.destroyAllWindows()
