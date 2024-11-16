import cv2
import mediapipe
import pyautogui

capture_hands = mediapipe.solutions.hands.Hands()
drawing_option = mediapipe.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
camera = cv2.VideoCapture(0)
x1 = y1 = x2 = y2 = 0
while True:
    _,image = camera.read()
    
    image_height, image_width, _ = image.shape
    image = cv2.flip(image,1)
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output_hands = capture_hands.process(rgb_image)
    all_hands = output_hands.multi_hand_landmarks
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(image,hand)
            one_hand_landmarks = hand.landmark
            for id, lm in enumerate(one_hand_landmarks):
                x = int(lm.x * image_width)
                y = int(lm.y * image_height) 
                #print(x,y)
                if id==8:
                    mouse_x = int ((screen_width / image_width * x))
                    mouse_y = int ((screen_height / image_height * y))
                    cv2.circle(image,(x,y),10,(0.255,255))
                    pyautogui.moveTo(mouse_x, mouse_y)
                    x1 = x
                    y1 = y
                if id==4:
                    x2 = x
                    y2 = y
                    cv2.circle(image,(x,y),10,(0.255,255))
                if id==20:
                    x3 = x
                    y3 = y
                    cv2.circle(image,(x,y),10,(0.255,255))
                
        dist1 = y2 - y1
        print(dist1)
        if(dist1<24):
            pyautogui.click()
            print("Clicked")
            
        # dist2 = y2-y3      
        # print(dist2)
        # if(dist2<5):
        #     pyautogui.hold
        #     print('scrolled')
            
          
            
            
            
    cv2.imshow("Hand Movement Video Capture", image)
    key = cv2.waitKey(1)
    if key == 27:
        break
camera.release()
print('Program Closed')
cv2.destroyAllWindows()

