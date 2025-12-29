import cv2
import numpy as np
import hand_detector as htm

BRUSH_THICKNESS = 15
ERASER_THICKNESS = 100
IMAGE_PATH = "header.png"

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.HandDetector(detection_con=0.85, max_hands=1)

img_canvas = np.zeros((720, 1280, 3), np.uint8)

draw_color = (255, 0, 255)
xp, yp = 0, 0

while True:
    success, img = cap.read()
    if not success:
        break
    img = cv2.flip(img, 1)

    img = detector.find_hands(img)
    lm_list = detector.find_position(img, draw=False)

    if len(lm_list) != 0:
        x1, y1 = lm_list[8][1:]
        x2, y2 = lm_list[12][1:]

        fingers = detector.fingers_up()
        
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("Selection Mode")
            if y1 < 125:
                if 250 < x1 < 450:
                    draw_color = (255, 0, 255)
                elif 550 < x1 < 750:
                    draw_color = (255, 0, 0)
                elif 800 < x1 < 950:
                    draw_color = (0, 255, 0)
                elif 1050 < x1 < 1200:
                    draw_color = (0, 0, 0)
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), draw_color, cv2.FILLED)

        if fingers[1] and not fingers[2]:
            print("Drawing Mode")
            cv2.circle(img, (x1, y1), 15, draw_color, cv2.FILLED)
            
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            thickness = ERASER_THICKNESS if draw_color == (0, 0, 0) else BRUSH_THICKNESS
            
            cv2.line(img_canvas, (xp, yp), (x1, y1), draw_color, thickness)

            xp, yp = x1, y1
        
        if not fingers[1] and not fingers[2]:
            xp, yp = 0, 0

    img_gray = cv2.cvtColor(img_canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
    
    img = cv2.bitwise_and(img, img_inv)
    img = cv2.bitwise_or(img, img_canvas)

    try:
        header = cv2.imread(IMAGE_PATH)
        img[0:125, 0:1280] = header
    except:
        pass

    cv2.imshow("Virtual Painter", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()