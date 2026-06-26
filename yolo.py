# ---------------------------------- NEW GUI ADVANCE PREVIOUS IS ALSO WORK FINE ------------------------------------------------------

import sys
import cv2
import numpy as np
import easyocr
from ultralytics import YOLO
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog
from PySide6.QtGui import QPixmap, QImage, QPalette, QBrush
from PySide6.QtCore import Qt, QSize

# Load YOLO + OCR
model = YOLO("best.pt")
reader = easyocr.Reader(['en'], gpu=False)


class ANPRApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🚘 Futuristic ANPR System")
        self.setGeometry(150, 100, 1100, 800)

        # === Set Futuristic Background Image ===
        # Create a palette but don't set the pixmap here
        palette = QPalette()
        self.setPalette(palette)
        
        # Call resizeEvent manually once to set the initial background
        self.resizeEvent(None)


        # Upload Button
        self.upload_btn = QPushButton("📂 Upload Image", self)
        self.upload_btn.setGeometry(220, 600, 220, 60)
        self.upload_btn.setStyleSheet(self.button_style())
        self.upload_btn.clicked.connect(self.upload_image)

        # Detect Button
        self.detect_btn = QPushButton("🔍 Detect Number Plate", self)
        self.detect_btn.setGeometry(460, 600, 280, 60)
        self.detect_btn.setStyleSheet(self.button_style())
        self.detect_btn.clicked.connect(self.detect_plate)

        # Image Display Box
        self.image_label = QLabel(self)
        self.image_label.setGeometry(100, 40, 900, 520)
        self.image_label.setStyleSheet("""
            background-color: #000;
            border: 3px solid #00E5FF;
            border-radius: 20px;
        """)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Result Box (Bigger Font)
        self.result_label = QLabel("Detected Number: ---", self)
        self.result_label.setGeometry(220, 690, 520, 70)
        self.result_label.setStyleSheet("""
            background-color: rgba(10, 20, 40, 200);
            border: 3px solid #00E5FF;
            border-radius: 20px;
            font-size: 32px;
            font-weight: bold;
            color: #00FFFF;
            padding: 12px;
        """)
        self.result_label.setAlignment(Qt.AlignCenter)

        self.current_image = None
    
    def resizeEvent(self, event):
        # Get the new size of the window
        new_size = self.size()
        # Reload the pixmap and scale it to the new size
        bg_pixmap = QPixmap("bg11.jpeg") 
        scaled_pixmap = bg_pixmap.scaled(new_size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        
        # Get the QPalette and update the background brush
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
        self.setPalette(palette)
        
        # Call the parent's resizeEvent
        super().resizeEvent(event)

    def button_style(self):
        """Hover effect style"""
        return """
            QPushButton {
                background-color: #1E1E2E;
                color: white;
                border: 2px solid #00FFFF;
                border-radius: 12px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00FFFF;
                color: black;
                border: 2px solid #FFFFFF;
            }
        """

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            self.current_image = cv2.imread(file_path)
            if self.current_image is not None:
                self.display_image(self.current_image)
                self.result_label.setText("Detected Number: ...")

    def display_image(self, img):
        if img is None:
            return
        h, w, ch = img.shape
        bytes_per_line = ch * w
        q_img = QImage(img.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(q_img).scaled(
            self.image_label.size(),
            Qt.KeepAspectRatio,  # Black bar fix
            Qt.SmoothTransformation
        )
        self.image_label.setPixmap(pixmap)

    def detect_plate(self):
        if self.current_image is None:
            self.result_label.setText("⚠️ Please upload an image first.")
            return

        results = model(self.current_image, verbose=False)

        found_plate = False
        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x, y, w, h = int(x1), int(y1), int(x2 - x1), int(y2 - y1)

                plate_roi = self.current_image[y:y + h, x:x + w]
                result = reader.readtext(plate_roi)

                if result:
                    text = result[0][1]
                    plate_number = "".join(filter(str.isalnum, text))
                    self.result_label.setText(f"✅ Detected Number: {plate_number}")

                    # Draw bigger rectangle + bigger text
                    cv2.rectangle(self.current_image, (x, y), (x + w, y + h), (0, 255, 0), 4)
                    cv2.putText(self.current_image, plate_number, (x, y - 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 0), 6)

                    self.display_image(self.current_image)
                    found_plate = True
                    break
            if found_plate:
                break

        if not found_plate:
            self.result_label.setText("❌ No Number Plate Detected.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ANPRApp()
    window.show()
    sys.exit(app.exec())