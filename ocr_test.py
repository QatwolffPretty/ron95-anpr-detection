from ultralytics import YOLO
import cv2
import numpy as np
from paddleocr import PaddleOCR
import requests
import json
import os

IMAGE_PATH = 'test_plate.jpg'
YOLO_MODEL_PATH = 'runs/detect/train/weights/best.pt'
API_ENDPOINT = 'http://localhost:8000/api/plates/'
CONFIDENCE_THRESHOLD = 0.4
DETECTION_CONFIDENCE = 0.3
PADDING = 10

model = YOLO(YOLO_MODEL_PATH)
ocr = PaddleOCR(use_textline_orientation=True, lang='en')

results = model.predict(IMAGE_PATH, imgsz=640, conf=DETECTION_CONFIDENCE)
boxes = results[0].boxes

if not boxes or len(boxes) == 0:
    print("[ERROR] No objects detected.")
    exit()

image = cv2.imread(IMAGE_PATH)
h_img, w_img = image.shape[:2]

plate_crop = None
max_area = 0
for box in boxes:
    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
    area = (x2 - x1) * (y2 - y1)
    if area > max_area:
        max_area = area
        x1_p, y1_p = max(x1 - PADDING, 0), max(y1 - PADDING, 0)
        x2_p, y2_p = min(x2 + PADDING, w_img), min(y2 + PADDING, h_img)
        plate_crop = image[y1_p:y2_p, x1_p:x2_p]

if plate_crop is None:
    print("[ERROR] Failed to crop plate region.")
    exit()

cv2.imwrite("temp_crop.jpg", plate_crop)
cv2.imshow("Plate Crop", plate_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

ocr_results = ocr.ocr("temp_crop.jpg")
print("[DEBUG] Raw OCR Results:")
print(ocr_results)

texts = []
confidences = []

if isinstance(ocr_results, list) and len(ocr_results) > 0 and isinstance(ocr_results[0], dict):
    rec_texts = ocr_results[0].get('rec_texts', [])
    rec_scores = ocr_results[0].get('rec_scores', [])
    if rec_texts and rec_scores and len(rec_texts) == len(rec_scores):
        texts = rec_texts
        confidences = rec_scores

if not texts or not confidences:
    print("[ERROR] OCR did not return valid results.")
    exit()

avg_conf = sum(confidences) / len(confidences)
print(f"[DEBUG] OCR result: '{' '.join(texts)}' with avg confidence {avg_conf:.2f}")

if avg_conf < CONFIDENCE_THRESHOLD:
    print(f"[SKIP] Low confidence ({avg_conf:.2f})")
    exit()

plate_number = ''.join(texts).replace(" ", "").upper()
data = {"plate_number": plate_number}
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(API_ENDPOINT, data=json.dumps(data), headers=headers)
    if response.status_code == 201:
        print(f"[SUCCESS] Plate logged: {plate_number}")
    else:
        print(f"[FAILURE] API error {response.status_code}: {response.text}")
except Exception as e:
    print(f"[ERROR] API request failed: {e}")

if os.path.exists("temp_crop.jpg"):
    os.remove("temp_crop.jpg")
