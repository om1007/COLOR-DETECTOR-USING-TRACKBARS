import numpy as np
import cv2



def empty(a):
    pass


# imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)

cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",0,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)
cv2.createTrackbar("Val Min","Trackbars",0,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)



while True :

    img = cv2.imread(r"do.png")
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max","Trackbars")
    v_min = cv2.getTrackbarPos("Val Min","Trackbars")
    v_max = cv2.getTrackbarPos("Val Max","Trackbars")
    

    print(h_min, h_max, s_min,s_max, v_min, v_max )

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(imgHSV,lower,upper)

    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Original Image", img)
    cv2.imshow("hsv img",imgHSV)
    cv2.imshow("mask",mask)
    cv2.imshow("imgResult", imgResult)

    # cv2.imshow("HSV Image", imgHSV)
    cv2.waitKey(1)  # Wait for a key press
    # if key == a:  # Escape key to quit
    #     break

    # cv2.destroyAllWindows()  # Close all windows
 