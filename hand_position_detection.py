import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    # checking if hand is detected
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:  # for each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                if id == 20:
                    # image, coordinates, radius, color (magenta), fill
                    cv2.circle(image, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS,
                                  landmark_drawing_spec=mpDraw.DrawingSpec(
                                      color=(0, 0, 255), thickness=2, circle_radius=2),
                                  connection_drawing_spec=mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2))

    cv2.imshow("Output", image)
    cv2.waitKey(1)


# 0. WRIST

# 1. THUMB_CMC
# 2. THUMB_MCP
# 3. THUMB_IP
# 4. THUMB_TIP

# 5.INDEX_FINGER_MCP
# 6.INDEX_FINGER_PIP
# 7. INDEX_FINGER_DIP
# 8.INDEX_FINGER_TIP

# 9. MIDDLE_FINGER_MCP
# 10. MIDDLE_FINGER_PIP
# 11. MIDDLE_FINGER_DIP
# 12. MIDDLE_FINGER_TIP

# 13. RING_FINGER_MCP
# 14. RING_FINGER_PIP
# 15. RING_FINGER_DIP
# 16. RING_FINGER_TIP

# 17. PINKY_MCP
# 18. PINKY_PIP
# 19. PINKY_DIP
# 20. PINKY_TIP
