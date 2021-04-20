import cv2
import numpy as np
from primesense import openni2
from primesense import _openni2 as c_api

openni2.initialize()
dev = openni2.Device.open_any()
depth_stream = dev.create_depth_stream()
print( dev.get_device_info())

depth_stream.start()
depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_1_MM, resolutionX = 640, resolutionY = 480, fps = 30))
print(dev.is_image_registration_mode_supported(c_api.OniImageRegistrationMode.ONI_IMAGE_REGISTRATION_DEPTH_TO_COLOR ))
print(dev.set_image_registration_mode(c_api.OniImageRegistrationMode.ONI_IMAGE_REGISTRATION_DEPTH_TO_COLOR))
while True:
	frame = depth_stream.read_frame()
	frame_data = frame.get_buffer_as_uint8()
	img = np.frombuffer(frame_data, dtype = np.uint8)
	img.reshape(640,960)
    cv.imshow("1",img)
	cv2.waitKey(34)
openni2.unload()
