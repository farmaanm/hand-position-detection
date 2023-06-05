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

                cv2.putText(image, str(id), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2) # image, text, coordinates, font, text scale, color (magenta), thickness
                
                if id == 20:
                    cv2.circle(image, (cx, cy), 10, (255, 0, 255), cv2.FILLED) # image, coordinates, radius, color (magenta), fill

                if id == 0:
                    id_0_x, id_0_y = cx, cy
                if id == 1:
                    id_1_x, id_1_y = cx, cy
                if id == 2:
                    id_2_x, id_2_y = cx, cy
                if id == 3:
                    id_3_x, id_3_y = cx, cy
                if id == 4:
                    id_4_x, id_4_y = cx, cy
                if id == 5:
                    id_5_x, id_5_y = cx, cy
                if id == 6:
                    id_6_x, id_6_y = cx, cy
                if id == 7:
                    id_7_x, id_7_y = cx, cy
                if id == 8:
                    id_8_x, id_8_y = cx, cy
                if id == 9:
                    id_9_x, id_9_y = cx, cy
                if id == 10:
                    id_10_x, id_10_y = cx, cy
                if id == 11:
                    id_11_x, id_11_y = cx, cy
                if id == 12:
                    id_12_x, id_12_y = cx, cy
                if id == 13:
                    id_13_x, id_13_y = cx, cy
                if id == 14:
                    id_14_x, id_14_y = cx, cy
                if id == 15:
                    id_15_x, id_15_y = cx, cy
                if id == 16:
                    id_16_x, id_16_y = cx, cy
                if id == 17:
                    id_17_x, id_17_y = cx, cy
                if id == 18:
                    id_18_x, id_18_y = cx, cy
                if id == 19:
                    id_19_x, id_19_y = cx, cy
                if id == 20:
                    id_20_x, id_20_y = cx, cy

            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS,
                                  landmark_drawing_spec=mpDraw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),
                                  connection_drawing_spec=mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2))
            
            # Thumbs up
            if (10 < abs(id_2_y - id_5_y) and abs(id_2_y - id_5_y) < 30 and abs(id_5_x - id_8_x) < 50 and id_4_y < id_0_y):
                cv2.putText(image, "Thumbs Up", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Thumbs down
            if (10 < abs(id_2_y - id_5_y) and abs(id_2_y - id_5_y) < 30 and abs(id_5_x - id_8_x) < 50 and id_4_y > id_0_y):
                cv2.putText(image, "Thumbs Down", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


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
