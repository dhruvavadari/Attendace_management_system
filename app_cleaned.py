
import cv2
import face_recognition
import os
import streamlit as st

def load_known_faces(directory="images"):
    encodings = []
    names = []
    for filename in os.listdir(directory):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(directory, filename)
            image = face_recognition.load_image_file(image_path)
            face_encs = face_recognition.face_encodings(image)
            if face_encs:
                encodings.append(face_encs[0])
                names.append(os.path.splitext(filename)[0])
            else:
                st.warning(f"No face found in {filename}")
    return encodings, names

def main():
    st.title("Real-Time Face Recognition")
    run = st.checkbox("Start Webcam")

    if run:
        known_encodings, known_names = load_known_faces()
        cap = cv2.VideoCapture(0)

        stframe = st.empty()

        while True:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to access webcam")
                break

            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            for face_encoding, face_location in zip(face_encodings, face_locations):
                matches = face_recognition.compare_faces(known_encodings, face_encoding)
                face_distances = face_recognition.face_distance(known_encodings, face_encoding)
                best_match_index = face_distances.argmin() if face_distances.size > 0 else None

                name = "Unknown"
                if best_match_index is not None and matches[best_match_index]:
                    name = known_names[best_match_index]

                top, right, bottom, left = [v * 4 for v in face_location]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

            stframe.image(frame, channels="BGR")

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
