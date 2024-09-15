import pyautogui
import cv2
import numpy as np

def screen_recorder(output_file, fps=10):
    
    screen_width, screen_height = pyautogui.size()

  
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_file, fourcc, fps, (screen_width, screen_height))

    print("Recording... ctr+cto stop.")
    
    try:
        while True:
   
            screenshot = pyautogui.screenshot()

            
            frame = np.array(screenshot)

            
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            
            out.write(frame)
    except KeyboardInterrupt:
        print("Recording stop.")

    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    screen_recorder("screen_recording.avi")
