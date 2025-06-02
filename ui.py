import cv2
import streamlit as st
import os
import face_recognition

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

def addNewPerson(name):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    DIR = 'images'
    name=st.text_input("Enter your name")
    nextid = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    cv2.imwrite('images/{}.jpg'.format(name), frame)
    print(" ")
    if os.path.isfile(os.path.join(DIR, '{}.jpg'.format(name))):
        st.write("You have successfully registered!")

def start_webcam():
    cap = cv2.VideoCapture(0)
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
                    st.write("True: Face matches with " + faces_names[match_index])
                    break
                else:
                    addNewPerson(st.text_input("enter your name"))
                    
        cap.release()
        cv2.destroyAllWindows()

st.title("Face recognition with Streamlit")
st.write("Welcome to the face recognition app.")
if st.button('Scan Face'):
    start_webcam()
