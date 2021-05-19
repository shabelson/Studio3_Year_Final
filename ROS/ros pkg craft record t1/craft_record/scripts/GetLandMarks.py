#!/home/shabelson/github/Studio3_Year_Final/Python/ROS/env/tvenv3/bin/python
import mediapipe as mp
import cv2 as cv
import copy





class LandMarkMaker(object):
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_holistic = mp.solutions.holistic
        self.mp_drawing.DrawingSpec(color=(0,0,255),thickness= 2,circle_radius=2)
        self.holistic = self.mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.image = []
        self.lmImg = []
        self.pixels = []
    def MakeLM(self,image):

        #debug_image = copy.deepcopy(frame)
        #image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = self.holistic.process(image)
        #image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        # 1. Draw face landmarks
        #mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS,
        #                          mp_drawing.DrawingSpec(color=(80, 110, 10), thickness=1, circle_radius=1),
        #                          mp_drawing.DrawingSpec(color=(80, 256, 121), thickness=1, circle_radius=1)
        #                          )
        # 2. Right hand
        # mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
        #                          mp_drawing.DrawingSpec(color=(80, 22, 10), thickness=2, circle_radius=4),
        #                          mp_drawing.DrawingSpec(color=(80, 44, 121), thickness=2, circle_radius=2)
        #                          )
        # 3. Left Hand
        # mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
        #                          mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
        #                          mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=2, circle_radius=2)
        #                          )
        # 4. Pose Detections
        try:
            self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS,
                                  self.mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4),
                                  self.mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                  )
            right_waist = results.pose_landmarks.landmark[24]
            right_shoulder = results.pose_landmarks.landmark[12]
            right_elbow = results.pose_landmarks.landmark[14]
            right_wrist = results.pose_landmarks.landmark[16]
            
            self.pixels = []
            for lm in self.landMarks:
                newpt =  self.mp_drawing._normalized_to_pixel_coordinates(lm.x, lm.y, 640, 480)
                self.pixels.append(newpt)
        
        except:
            right_waist = []
            right_shoulder = []
            right_elbow = []
            right_wrist = []
        self.landMarks = [right_waist,right_shoulder,right_elbow,right_wrist]
        self.lmImg = image

