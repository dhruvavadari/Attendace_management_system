import cv2
import face_recognition
import datetime
import streamlit as st
import os

def compare_faces_in_webcam_and_directory():
    # Load the faces to be recognized from a directory
    faces_to_recognize = []
    faces_encodings = []
    faces_names = []
    directory = "images"
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            image = face_recognition.load_image_file(os.path.join(directory, filename))
            encoding = face_recognition.face_encodings(image)[0]
            faces_encodings.append(encoding)
            faces_names.append(os.path.splitext(filename)[0])

    # Start the webcam
    cap = cv2.VideoCapture(0)
    st.write("Press q to stop the video.")
    while True:
        ret, frame = cap.read()
        if ret:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            for face_encoding in face_encodings:
                distances = face_recognition.face_distance(faces_encodings, face_encoding)
                min_distance = min(distances)
                if min_distance < 0.6:
                    match_index = distances.argmin()
                    st.write(f"True: Face matches with {faces_names[match_index]} at {datetime.datetime.now()}")
                    break
            else:
                def addNewPerson(name):
                    cap = cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    DIR = 'images'
                    nextid = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
                    #cv2.imshow('frame', frame)
                    cv2.imwrite('images/{}_{}.jpg'.format(nextid + 1, name), frame)
                    st.write(" " + str(nextid + 1))
        addNewPerson(input("Set name of new person: "))
                    
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

st.title("Face Recognition App")
st.write("This app compares your face in the webcam with the faces in the directory and outputs if a match is found.")
compare_faces_in_webcam_and_directory()
