
# Attendance Management System using Face Recognition

This project is a face recognition-based attendance management system developed using OpenCV, face_recognition, Streamlit, and various supporting tools. It supports real-time face detection from webcam input and matches against a database of pre-encoded images to log attendance.

---

## 🔧 Features

- Real-time face detection using webcam
- Face matching using `face_recognition` library
- Image encoding and storage using `pickle`
- Interactive Streamlit web app interface
- Visual overlays for UI and status
- Easily extendable for logging, database storage, and ID verification

---

## 📂 Project Structure

```
attendance-management-system/
├── 1/
│   ├── main.py                # Real-time recognition script
│   ├── enoder_cleaned.py      # Encode student images
│   ├── Encode_file.p          # Saved encodings
│   ├── Images/                # Student face images
│   └── Resources/             # UI and background images
├── 2/source-code-face-recognition/
│   ├── app_cleaned.py         # Streamlit face recognition app
│   ├── image_comparison.py    # (to be cleaned)
│   ├── main_video.py          # (to be cleaned)
│   ├── simple_facerec.py      # Utilities for recognition
│   └── ...
```

---

## 📦 Libraries and Dependencies

Make sure the following libraries are installed. You can install them with `pip`:

```bash
pip install opencv-python
pip install face_recognition
pip install numpy
pip install streamlit
pip install dlib
```

> 💡 Note: `dlib` might require CMake and C++ build tools on your system to install properly.

---

## 🚀 How to Run

### Encode Images (Step 1):
1. Add your images to the `Images/` folder (ensure face is clearly visible).
2. Run:
```bash
python enoder_cleaned.py
```

### Launch Webcam Recognition (Step 2):
```bash
python main.py
```

### Or use the Streamlit App:
```bash
streamlit run app_cleaned.py
```

---

## 📸 Example Use Case

- Place face images of students in the `Images/` folder
- Run the encoder to generate encodings
- Start the webcam to detect faces
- The recognized student ID will be printed in the terminal

---

## 🧠 Future Improvements

- Attendance log CSV/Database integration
- Student profile linking
- Time-based attendance windows
- Notification or reporting system

---

## 👨‍💻 Author

Developed by **Dhruva Vadari**

---

## 📃 License

MIT License
