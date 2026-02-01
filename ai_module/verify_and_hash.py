import cv2
import pytesseract
import hashlib
from PIL import Image

# 1. Point to your Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def process_certificate(image_path):
    # 2. Load and Pre-process image (Grayscale improves OCR)
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 3. Extract Text using AI (OCR)
    extracted_text = pytesseract.image_to_string(gray)
    print(f"--- Extracted Text ---\n{extracted_text}\n----------------------")

    # 4. Verification Logic (Simple example: check if 'University' is in text)
    if "University" not in extracted_text:
        return None, "Verification Failed: Not a valid university document."

    # 5. Generate unique SHA-256 Hash for the Blockchain
    # We hash the extracted text so even a tiny typo creates a different hash
    file_hash = hashlib.sha256(extracted_text.encode()).hexdigest()
    
    return file_hash, "Success"

# Test it
hash_result, status = process_certificate("test_degree.png")
print(f"Status: {status}")
if hash_result:
    print(f"Final Hash for Blockchain: 0x{hash_result}")