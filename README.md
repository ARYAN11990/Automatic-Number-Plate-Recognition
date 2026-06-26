# 🚘 Automatic Number Plate Recognition (ANPR) System

An AI-powered **Automatic Number Plate Recognition (ANPR)** desktop application built using **Python, YOLOv8, EasyOCR, OpenCV, and PySide6**.

This application detects vehicle number plates from uploaded images using a custom-trained YOLOv8 model and extracts the license plate text using EasyOCR. The project features a modern graphical user interface (GUI) that allows users to upload an image and instantly view the detected number plate.

---

## 📌 Features

- 🚗 Automatic Number Plate Detection
- 🤖 Custom YOLOv8 Model for Object Detection
- 🔍 Text Recognition using EasyOCR
- 🖥️ Modern Desktop GUI built with PySide6
- 📂 Upload Images from Local Storage
- 📍 Automatic Bounding Box Detection
- 📝 Displays Detected Number Plate
- ⚡ Fast and Accurate Detection
- 🎨 Futuristic User Interface

---

## 🛠️ Technologies Used

- Python
- YOLOv8 (Ultralytics)
- EasyOCR
- OpenCV
- PySide6
- NumPy
- PyTorch

---

## 📂 Project Structure

```
ANPR_Project/

│── yolo.py                 # Main application (Run this file)
│── main.py                 # Older implementation
│── ocr.py                  # OCR testing script
│── best.pt                 # Trained YOLOv8 model
│── bg11.jpeg               # GUI background image
│── requirements.txt
│── README.md
│── __pycache__/
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ARYAN11990/Automatic-Number-Plate-Recognition.git

cd Automatic-Number-Plate-Recognition
```

---

### 2️⃣ Create Virtual Environment (Optional)

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually

```bash
pip install ultralytics easyocr opencv-python numpy PySide6 torch torchvision
```

---

## ▶️ Run the Project

Run the main application

```bash
python yolo.py
```

---

## 🚀 How to Use

1. Launch the application.
2. Click **Upload Image**.
3. Select an image containing a vehicle.
4. Click **Detect Number Plate**.
5. The application will:
   - Detect the number plate using YOLOv8.
   - Extract the plate text using EasyOCR.
   - Display the detected number.
   - Draw a green bounding box around the number plate.

---

## 🧠 Working Pipeline

```
Input Image
      │
      ▼
YOLOv8 Detection
      │
      ▼
Crop Number Plate
      │
      ▼
EasyOCR
      │
      ▼
Extract Plate Number
      │
      ▼
Display Result on GUI
```

---

## 📦 Requirements

```
ultralytics
opencv-python
easyocr
numpy
PySide6
torch
torchvision
```

---

## 🎯 Applications

- Smart Parking Systems
- Vehicle Identification
- Toll Booth Automation
- Traffic Monitoring
- Security & Surveillance
- Automatic Gate Entry
- College & Campus Vehicle Management

---

## 🚀 Future Improvements

- 📹 Real-time Webcam Detection
- 🎥 Video File Detection
- 💾 Detection History
- ☁️ Database Integration
- 🌐 Web-based Version
- 📊 Vehicle Analytics Dashboard
- Multiple Number Plate Detection

---

## 📷 Sample Output

After uploading a vehicle image, the application:

- Detects the vehicle number plate.
- Draws a green bounding box.
- Reads the plate text using OCR.
- Displays the detected number inside the application.

*(You can add screenshots here later.)*

---

## 👨‍💻 Author

### Aryan Parmar

Computer Science Student

Interested in:

- Artificial Intelligence
- Machine Learning
- Computer Vision
- Python Development
- Web Development

GitHub:
https://github.com/ARYAN11990

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

## 📄 License

This project is developed for educational and learning purposes.
