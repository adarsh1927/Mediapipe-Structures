import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
print(dir(mp_drawing_styles))
mp_holistic = mp.solutions.holistic

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as holistic:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = holistic.process(image)

    # Draw landmark annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Draw
    mp_drawing.draw_landmarks(
        image,
        results.face_landmarks,
        mp_holistic.FACEMESH_CONTOURS,
        landmark_drawing_spec=None,
        connection_drawing_spec=mp_drawing_styles
        .get_default_face_mesh_contours_style())
    
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_holistic.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles
        .get_default_pose_landmarks_style())
    

    #Research
    print('\n---------------------landmarks list--------------------------')
    print('\n', 'results.pose_landmarks: ',type(results.pose_landmarks)) 
    print('\n', 'results.pose_landmarks.landmark: ',type(results.pose_landmarks.landmark)) # we will defenataly do it 

    print('\n-------------------mp_holistic----------------------------')

    print('\n', 'dir: ',dir(mp_holistic))    
    print('\n', 'data: ',mp_holistic)
    print('\n', 'type: ',type(mp_holistic))

    print('\n-------------------mp_holistic.POSE_CONNECTIONS----------------------------')

    print('\n', 'dir: ',dir(mp_holistic.POSE_CONNECTIONS))    
    print('\n', 'data: ',mp_holistic.POSE_CONNECTIONS)
    print('\n', 'type: ',type(mp_holistic.POSE_CONNECTIONS))

    print('\n--------------------getting the coordinates---------------------------')

    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE.value]

    print('\n--------------------mp_holistic.PoseLandmark---------------------------')

    print('\n', 'dir: ',dir(mp_holistic.PoseLandmark))
    print('\n', 'data: ',mp_holistic.PoseLandmark)
    print('\n', 'type: ',type(mp_holistic.PoseLandmark))

    print('\n--------------------landmark name and index---------------------------')
    for parts in mp_holistic.PoseLandmark:
      parts.value
    
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Holistic', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()