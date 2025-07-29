from flask import Flask, request, render_template
from cryptography.fernet import Fernet
import os, hashlib

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ENCRYPTED_FOLDER = 'encrypted'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)

# Load AES key
with open("secret.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    with open(file_path, 'rb') as f:
        encrypted = fernet.encrypt(f.read())
    
    encrypted_path = os.path.join(ENCRYPTED_FOLDER, file.filename + '.enc')
    with open(encrypted_path, 'wb') as f:
        f.write(encrypted)

    file_hash = hashlib.sha256(encrypted).hexdigest()

    return f"✅ File encrypted!<br>🔒 Encrypted path: {encrypted_path}<br>📎 SHA256 Hash: {file_hash}"
    
if __name__ == '__main__':
    app.run(debug=True)
