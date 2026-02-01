import cv2
import pytesseract
import os

# 1. Tesseract Path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HP\Documents\tess\tesseract.exe'
def test_ocr():
    # Get the exact folder where THIS script is saved
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "test_degree.png")
    
    print(f"Checking for image at: {image_path}")

    # Check if file exists before opening
    if not os.path.exists(image_path):
        print(f"❌ ERROR: 'test_degree.png' is NOT in the {script_dir} folder.")
        print(f"Files actually in this folder: {os.listdir(script_dir)}")
        return

    # 2. Load the image
    img = cv2.imread(image_path)
    if img is None:
        print("❌ ERROR: OpenCV could not decode the image. Is it a valid .png or .jpg?")
        return

    # 3. Process
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    print("\n✅ SUCCESS! Extracted Text:")
    print("-" * 30)
    print(text if text.strip() else "[No text detected in image]")
    print("-" * 30)

if __name__ == "__main__":
    test_ocr()