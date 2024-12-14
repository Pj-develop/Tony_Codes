import cv2  # OpenCV for video capture and image processing
import serial  # For serial communication
from cvzone.HandTrackingModule import HandDetector  # Hand detection module from cvzone

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize hand detector with confidence threshold and max number of hands
detector = HandDetector(detectionCon=0.5, maxHands=1)

# Initialize serial communication (adjust 'COM7' to your port and '9600' to your baud rate)
bt = serial.Serial('COM7', 9600)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Flip the frame horizontally for a mirror effect
    flip_both = cv2.flip(frame, 1)

    # Detect hands in the frame
    hands, frame = detector.findHands(frame)

    # Check if any hands are detected
    if not hands:
        print("nothing")  # If no hands detected, print "nothing"
    else:
        # Get data of the first detected hand
        hand1 = hands[0]

        # Get which fingers are up
        fingers = detector.fingersUp(hand1)

        # Count the number of fingers that are up
        count = fingers.count(1)
        print(count)  # Print the count of fingers up

        # Determine the command based on the number of fingers up
        if count == 1:
            command = 'F'  # Command for forward
        elif count == 2:
            command = 'B'  # Command for backward
        elif count == 3:
            command = 'L'  # Command for left
        elif count == 4:
            command = 'R'  # Command for right
        else:
            command = 'S'  # Command for stop

        print(f"Command: {command}")  # Print the command being sent
        bt.write(command.encode("utf-8"))  # Send the command over Bluetooth

    # Display the video feed with detected hands
    cv2.imshow("FRAME", frame)

    # Break the loop if the ESC key (27) is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
