import cv2
import numpy as np
from primesense import openni2
from primesense import _openni2 as c_api

# Initialize the depth device
openni2.initialize()
dev = openni2.Device.open_any()

# Start the depth stream
depth_stream = dev.create_depth_stream()
rgb_stream = dev.create_color_stream()

depth_stream.start()
depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_100_UM, resolutionX = 640, resolutionY = 480, fps = 30))

rgb_stream.start()
rgb_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_100_UM, resolutionX = 640, resolutionY = 480, fps = 30))
#rgb_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888, resolutionX = 480, resolutionY = 640, fps = 30))

# Function to return some pixel information when the OpenCV window is clicked
refPt = []
selecting = False


if (rgb_stream.camera != None):
	rgb_stream.camera.set_auto_exposure(bAutoExposure)
	rgb_stream.camera.set_exposure(exposure)


def point_and_shoot(event, x, y, flags, param):
                global refPt, selecting
                if event == cv2.EVENT_LBUTTONDOWN:
                                print ("Mouse Down")
                                refPt = [(x,y)]
                                selecting = True
                                print (refPt)
                elif event == cv2.EVENT_LBUTTONUP:
                                print ("Mouse Up")
                                refPt.append((x,y))
                                selecting = False
                                print (refPt)

# Initial OpenCV Window Functions
cv2.namedWindow("Depth Image")
cv2.setMouseCallback("Depth Image", point_and_shoot)

# Loop
while True:
                # Grab a new depth frame
                frame = depth_stream.read_frame()
                frame_data = frame.get_buffer_as_uint16()
                # Put the depth frame into a numpy array and reshape it
                img = np.frombuffer(frame_data, dtype=np.uint16)
                img.shape = (1, 480, 640)
                
                img = np.concatenate((img, img, img), axis=0)
                img = np.swapaxes(img, 0, 2)
                img = np.swapaxes(img, 0, 1)



                frame = rgb_stream.read_frame()
                frame_data = frame.get_buffer_as_uint16()
                
                colorPix = np.frombuffer(frame_data, dtype=np.uint16)
                colorPix.shape = (3, 640, 240)


                colorPix = np.concatenate((colorPix, colorPix, colorPix), axis=0)
                colorPix = np.swapaxes(colorPix, 0, 2)
                colorPix = np.swapaxes(colorPix, 0, 1)
                

                if len(refPt) > 1:
                                img = img.copy()
                                cv2.rectangle(img, refPt[0], refPt[1], (0, 255, 0), 2)
                                cv2.rectangle(colorPix, refPt[0], refPt[1], (0, 255, 0), 2)
                
                # Display the reshaped depth frame using OpenCV
                cv2.imshow("Depth Image", img)
                #cv2.imshow("Depth Image2", colorPix)
                
                key = cv2.waitKey(1) & 0xFF

                # If the 'c' key is pressed, break the while loop
                if key == ord("c"):
                                break

# Close all windows and unload the depth device
openni2.unload()
cv2.destroyAllWindows()