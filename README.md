# 🇲🇾 RON95 ANPR Detection System (Prototype)  
*By Siti Nur Afiqah Nadzim — KTTNDSTY*

This is a working prototype of an **Automatic Number Plate Recognition (ANPR)** system developed to support the Malaysian government's fuel subsidy enforcement efforts.

It is designed to detect **foreign-registered vehicles** at petrol stations using computer vision, and optionally restrict access to **RON95 petrol** based on regulatory policies.

---

## 🔧 Tech Stack
- 🐍 **Python** (`OpenCV`, `EasyOCR`) – Plate Detection  
- 🌐 **Django REST Framework** – API Backend for Plate Logging  
- 🧾 **MySQL** – Database Storage  
- 🖥️ **Node.js** *(Planned)* – Admin Dashboard *(WIP)*  
- 📱 **Termux Compatible** – For Android use  
- 🐧 **Linux & Windows Compatible**  

---

## 📂 Project Structure

```bash
ron95-anpr-detection/
├── anpr/
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── urls.py
│ └── views.py
├── backend/
│ ├── settings.py
│ └── urls.py
├── manage.py
├── ocr_test.py
├── README.md
└── requirements.txt
```
---

### ⚙️ Setup (Linux, Termux, Windows)

#### 1. Clone the Repository

```bash
git clone https://github.com/QatwolffPretty/ron95-anpr-detection.git
cd ron95-anpr-detection
```
---

#### 2. Create a Virtual Environment
Linux/Termux
```bash
python3 -m venv venv
source venv/bin/activate
```
Windows
```bash
python -m venv venv
venv\Scripts\activate
```
---

#### 3. Install Required Packages
```bash
pip install -r requirements.txt
```
---

#### 4. Setup your MySQL
Login to MySQL:
```bash
mysql -u root -p
```
Create the database and user:
```bash
CREATE DATABASE anpr_db;
CREATE USER 'django'@'localhost' IDENTIFIED BY 'yourpassword';
GRANT ALL PRIVILEGES ON anpr_db.* TO 'django'@'localhost';
FLUSH PRIVILEGES;
```
---

#### 5. Run Django Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
---

#### 6. Create Superuser (Optional but Recommended)
```bash
python manage.py createsuperuser
```
Set your desired username, email, and password.
---

#### 7. Run Django Development Server
```bash
python manage.py runserver
```
Access Admin Panel: http://127.0.0.1:8000/admin

View Plate Logs: http://127.0.0.1:8000/api/plates/
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
