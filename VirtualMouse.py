import cv2
import numpy as np
import time
import HandTracking as ht
import autopy
import screen_brightness_control as sbc

### Variables Declaration
pTime = 0
width = 640
height = 480
frameR = 0              
smoothening = 7         
prev_x, prev_y = 0, 0
curr_x, curr_y = 0, 0

click_cooldown = 0
click_delay = 0.3       # 300ms delay between clicks

brightness_cooldown = 0
brightness_delay = 0.2

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

detector = ht.handDetector(maxHands=1, detectionCon=0.8, trackCon=0.8)
screen_width, screen_height = autopy.screen.size()

print("Virtual Mouse Started!")
print("Controls:")
print("- Index finger up: Move cursor")
print("- Index + Middle finger up (pinch): Left Click")
print("- Index + Middle + Ring finger up: Right Click")
print("- All 5 fingers open: Increase Brightness")
print("- All fingers closed (fist): Decrease Brightness")
print("- Press 'q' to quit")

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture frame")
        continue
    
    img = cv2.flip(img, 1)  # Mirror image for more natural control
    img = detector.findHands(img)
    lmlist, bbox = detector.findPosition(img, draw=False)

    if len(lmlist) != 0:
        x1, y1 = lmlist[8][1:]  # Index finger tip
        x2, y2 = lmlist[12][1:]  # Middle finger tip
        x3, y3 = lmlist[16][1:]  # Ring finger tip
        x_thumb, y_thumb = lmlist[4][1:]  # Thumb tip

        fingers = detector.fingersUp()
        
        if frameR > 0:
            cv2.rectangle(img, (frameR, frameR), 
                         (width - frameR, height - frameR), 
                         (255, 0, 255), 2)
        
        if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0:
            x3 = np.interp(x1, (frameR, width - frameR), (0, screen_width))
            y3 = np.interp(y1, (frameR, height - frameR), (0, screen_height))

            curr_x = prev_x + (x3 - prev_x) / smoothening
            curr_y = prev_y + (y3 - prev_y) / smoothening

            try:
                autopy.mouse.move(curr_x, curr_y)
                cv2.circle(img, (x1, y1), 10, (0, 255, 0), cv2.FILLED)
                cv2.putText(img, "Move Mode", (50, 50), 
                           cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            except Exception as e:
                pass

            prev_x, prev_y = curr_x, curr_y

        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0:
            length, img, lineInfo = detector.findDistance(8, 12, img, draw=True, r=10, t=2)
            
            if length < 35:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 
                          15, (0, 255, 0), cv2.FILLED)
                
                current_time = time.time()
                if current_time - click_cooldown > click_delay:
                    try:
                        autopy.mouse.click()
                        click_cooldown = current_time
                        cv2.putText(img, "LEFT CLICK", (50, 50), 
                                   cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
                    except Exception as e:
                        pass
            else:
                cv2.putText(img, "Click Mode", (50, 50), 
                           cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)

        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 0:
            length, img, lineInfo = detector.findDistance(8, 16, img, draw=True, r=10, t=2)
            
            if length < 50:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 
                          15, (0, 0, 255), cv2.FILLED)
                
                current_time = time.time()
                if current_time - click_cooldown > click_delay:
                    try:
                        autopy.mouse.click(autopy.mouse.Button.RIGHT)
                        click_cooldown = current_time
                        cv2.putText(img, "RIGHT CLICK", (50, 50), 
                                   cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
                    except Exception as e:
                        pass
            else:
                cv2.putText(img, "Right Click Mode", (50, 50), 
                           cv2.FONT_HERSHEY_PLAIN, 2, (255, 165, 0), 2)

        current_time = time.time()
        
        if fingers == [1, 1, 1, 1, 1]:
            if current_time - brightness_cooldown > brightness_delay:
                try:
                    current_brightness = sbc.get_brightness()[0]
                    new_brightness = min(100, current_brightness + 5)
                    sbc.set_brightness(new_brightness)
                    brightness_cooldown = current_time
                    cv2.putText(img, f"BRIGHTNESS UP: {new_brightness}%", (50, 50), 
                               cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 3)
                except Exception as e:
                    cv2.putText(img, "Brightness control error", (50, 50), 
                               cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        
        elif fingers == [0, 0, 0, 0, 0]:
            if current_time - brightness_cooldown > brightness_delay:
                try:
                    current_brightness = sbc.get_brightness()[0]
                    new_brightness = max(0, current_brightness - 5)
                    sbc.set_brightness(new_brightness)
                    brightness_cooldown = current_time
                    cv2.putText(img, f"BRIGHTNESS DOWN: {new_brightness}%", (50, 50), 
                               cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
                except Exception as e:
                    cv2.putText(img, "Brightness control error", (50, 50), 
                               cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
    else:
        cv2.putText(img, "No Hand Detected", (50, 50), 
                   cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (width - 150, 50), 
               cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv2.imshow("Virtual Mouse", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Virtual Mouse Stopped!")