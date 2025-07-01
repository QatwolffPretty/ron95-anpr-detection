import easyocr
import requests
import re
from datetime import datetime

API_URL = 'http://localhost:8000/api/plates/'
CONFIDENCE_THRESHOLD = 0.5
image_path = 'test_plate.jpg'

reader = easyocr.Reader(['en'], gpu=False)
results = reader.readtext(image_path)

def clean_plate(text):
    text = text.upper().replace('I', '1').replace('O', '0')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def is_valid_plate(text):
    return re.match(r'^[A-Z]{1,3} ?[0-9]{1,4}$', text) or re.match(r'^[A-Z]{1,3} ?[A-Z]{1,3} ?[0-9]{1,4}$', text)

sorted_results = sorted(results, key=lambda x: x[0][0][0])

combined_line = []
for i, (bbox, text, conf) in enumerate(sorted_results):
    cleaned = clean_plate(text)
    combined_line.append((cleaned, conf))

joined_text = " ".join([item[0] for item in combined_line])
avg_conf = sum([item[1] for item in combined_line]) / len(combined_line)

print(f"[DEBUG] Raw OCR: '{joined_text}' with avg confidence {avg_conf:.2f}")

if avg_conf < CONFIDENCE_THRESHOLD:
    print(f"[SKIP] Average confidence too low: {avg_conf:.2f}")
elif not is_valid_plate(joined_text):
    print(f"[SKIP] Invalid format: {joined_text}")
else:
    print(f"Detected: {joined_text}, Confidence: {avg_conf:.2f}")

    data = {
        'plate_number': joined_text,
        'country': 'MY',
        'confidence': round(avg_conf, 2),
        'timestamp': datetime.now().isoformat()
    }

    try:
        response = requests.post(API_URL, json=data)
        print("[✅] API response:", response.json())
    except Exception as e:
        print("[❌] Failed to send to API:", str(e))
