import cv2
import numpy as np
import easyocr

plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
img = cv2.imread('car4.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

reader = easyocr.Reader(['en'], gpu=False)

plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

plate_number = "Could not recognize"

if len(plates) > 0:
    print(f"Number plate found! Processing {len(plates)} plate(s)...")
    for (x, y, w, h) in plates:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        plate_roi = img[y:y+h, x:x+w]
        if plate_roi.size == 0:
            print("Cropped plate region is empty. Skipping.")
            continue
        try:
            result = reader.readtext(plate_roi)
            if result:
                text = result[0][1]
                plate_number = "".join(filter(str.isalnum, text))
                print("Detected Number:", plate_number)
            else:
                print("No text detected by EasyOCR.")
        except Exception as e:
            print(f"OCR Error for this plate: {e}")
        font_scale = w / 250.0
        font_thickness = max(1, int(font_scale * 2))
        cv2.putText(img, plate_number, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 255, 0), font_thickness)
else:
    print("No number plate detected in the image.")

max_width = 800
(h, w) = img.shape[:2]
if w > max_width:
    r = max_width / float(w)
    dim = (max_width, int(h * r))
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

cv2.imshow('Original Image with Detected Plate', img)
cv2.waitKey(0)
cv2.destroyAllWindows()