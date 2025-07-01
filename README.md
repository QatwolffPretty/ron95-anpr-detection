# 🇲🇾 RON95 ANPR Detection System (Prototype)  
*By Siti Nur Afiqah Nadzim — KTTNDSTY*

This is a working prototype of an **Automatic Number Plate Recognition (ANPR)** system developed to support the Malaysian government's fuel subsidy enforcement efforts.

It is designed to detect **foreign-registered vehicles** at petrol stations using computer vision, and optionally restrict access to **RON95 petrol** based on regulatory policies.

---

## 🔧 Tech Stack
- 🐍 Python (OpenCV + EasyOCR) – Plate detection
- 🌐 Django REST – API backend for logging
- 🧾 MySQL – Database storage
- 🖥️ Node.js (planned) – Admin dashboard (WIP)
- 📱 Termux compatibility – For Android edge device testing

---

## 📂 Project Structure
ron95-anpr-detection/
├── plate-reader/         
#### Python EasyOCR for reading license plates

│   └── ocr_test.py       
#### Test script for recognition

├── backend/            
#### Django REST API

│   ├── recognition/     
#### Django app (models, views, serializers)

│   └── anpr_api/         
#### Project settings

├── dashboard/           
#### Node.js admin dashboard (coming soon)
└── README.md

---

## 🚀 How to Run (Termux)

```bash
pkg update
pkg install python git nodejs mariadb
pip install easyocr opencv-python django djangorestframework mysqlclient
cd plate-reader
python ocr_test.py
cd backend
python manage.py runserver
```
---

### 📄 `LICENSE` File (Demo Only)

```text
Copyright (c) 2025 Siti Nur Afiqah Nadzim

This project, including all source code and documentation, is provided for 
demonstration, educational, and proposal purposes only.

You are NOT permitted to:
- Commercially use this project or its code
- Deploy it in production environments
- Modify and redistribute it for profit
- Claim ownership of the concept or implementation

You ARE allowed to:
- Study and learn from the code
- Reference the project in academic or proposal work
- Request permission to collaborate or build upon the system

For commercial licensing, customization, or collaboration, please contact:
📧 slytheronyx97@gmail.com

All rights reserved.
```
