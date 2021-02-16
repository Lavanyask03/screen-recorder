# opencv docs => https://docs.opencv.org/4.3.0/dd/d43/tutorial_py_video_display.html
# imports
import cv2
import numpy as np
import pyautogui

SCREEN_SIZE = (1920,1080)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # In Windows: DIVX 
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (SCREEN_SIZE))
# 20.0 -> number of frames per second

# capture screenshots until user clicks 'q' and convert to numpy array
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    # convert color from BGR -> RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    # show the frame
    #cv2.imshow("screenshot",frame)
    # quit if user clicks 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# close everything 
out.release()
cv2.destroyAllWindows()
