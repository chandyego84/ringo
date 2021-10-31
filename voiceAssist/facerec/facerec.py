import face_recognition
import cv2
import numpy as np
import os
import glob

def faceRec():
    # get video reference
    video_capture = cv2.VideoCapture(0)
    # get files from trainingdata
    files = glob.glob("trainingdata/*.jpg")
    # get encodings from files
    known_face_encodings = []
    known_face_names = []
    for file in files:
        image = face_recognition.load_image_file(file)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(os.path.splitext(os.path.basename(file))[0])
    # start loop
    while True:
        # get frame from video
        ret, frame = video_capture.read()
        # convert to rgb
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # get face locations
        face_locations = face_recognition.face_locations(rgb_frame)
        # get face encodings
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        # loop over face encodings
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # get distances
            distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            # get best match
            best_match_index = np.argmin(distances)
            if distances[best_match_index] < 0.6:
                name = known_face_names[best_match_index]
            else:
                name = "Unknown"
            # draw rectangle
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # draw label
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        # show frame
        cv2.imshow('Video', frame)
        # quit on q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # release video
    video_capture.release()
    cv2.destroyAllWindows()

faceRec()