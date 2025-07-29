# 🔐 FUTURE_CS_03 - Secure File Sharing App

A simple Flask-based secure file sharing app that encrypts uploaded files using AES (via `cryptography.Fernet`) and computes SHA256 hash for integrity verification.

---

## 🚀 Features

- 🔐 AES encryption for uploaded files
- 🧮 SHA256 hash generation for integrity check
- 🌐 Flask UI for file uploads
- 📄 Sample file included for testing

---

## 🧪 How to Use

```bash
# 1. Clone the repo
git clone https://github.com/CyberRN-Mulla/FUTURE_CS_03.git
cd FUTURE_CS_03

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install required packages
pip install flask cryptography

# 4. Generate encryption key
python3 generate_key.py

# 5. Start the Flask server
python3 app.py

# 6. Then open your browser and go to http://127.0.0.1:5000

---

## 🧠 Developer
Godson Enruchi Chukwu (CyberRN-Mulla)
Abuja, Nigeria
