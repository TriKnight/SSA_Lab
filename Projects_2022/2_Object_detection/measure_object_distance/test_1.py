import cv2
from realsense_camera import *


# Load Realsense camera
rs = RealsenseCamera()

while True:
    # Get frame in real time from Realsense camera
    ret, bgr_frame, depth_frame = rs.get_frame_stream()
    
    #print(depth_frame) # Measure the distance in milimeters
    point_x, point_y = 500, 500
    distance = depth_frame[point_y,point_x]
    
    cv2.circle(bgr_frame, (point_x, point_y), 8, (255,0,0),-1)
    cv2.putText(bgr_frame,"{} mm".format(distance), (point_x + 10,point_y),0,1,(0,255,0),2)
    cv2.imshow("Depth frame", depth_frame)
    cv2.imshow("Bgr frame", bgr_frame)
    
    key= cv2.waitKey(1)
    if key == 27:
        break