import cv2
import pytesseract
import hashlib
import os

# 1. Tesseract Configuration
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HP\Documents\tess\tesseract.exe'

def generate_credential_hash(image_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, image_name)

    # 2. Extract Text
    img = cv2.imread(image_path)
    if img is None:
        return None, "Error: Image not found."
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    extracted_text = pytesseract.image_to_string(gray).strip()
    
    if not extracted_text:
        return None, "Error: No text detected for hashing."

    # 3. Create the Hash (The Blockchain Fingerprint)
    # We use SHA-256 to create a unique 64-character string
    credential_hash = hashlib.sha256(extracted_text.encode()).hexdigest()
    
    return f"0x{credential_hash}", extracted_text

if __name__ == "__main__":
    blockchain_hash, original_text = generate_credential_hash("test_degree.png")
    
    if blockchain_hash:
        print(f"✅ Text Extracted Successfully!")
        print(f"--- Extracted Content ---\n{original_text}\n------------------------")
        print(f"🚀 HASH FOR BLOCKCHAIN: {blockchain_hash}")
    else:
        print(blockchain_hash)