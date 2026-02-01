from PIL import Image, ImageDraw

def create_test_image():
    # Create a white image
    img = Image.new('RGB', (800, 400), color='white')
    d = ImageDraw.Draw(img)
    
    # Write some clear text for the AI to find
    text = "University Certificate\n\nStudent Name: John Doe\nDegree: Bachelor of Blockchain\nDate: 2026"
    
    # Draw the text in black
    # Note: Using default font; if it's too small, OCR might struggle, 
    # but it usually works for a base test.
    d.multiline_text((50, 50), text, fill=(0, 0, 0))
    
    # Save it exactly where test_ocr.py expects it
    img.save('test_degree.png')
    print("✅ Created 'test_degree.png' successfully in ai_module!")

if __name__ == "__main__":
    create_test_image()