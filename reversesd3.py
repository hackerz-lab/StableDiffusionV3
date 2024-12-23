import pytesseract
from PIL import Image
import os

# Ensure pytesseract knows where Tesseract is installed
# You may need to adjust the path if it's installed elsewhere
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def image_to_text(image_path):
    # Open the image using Pillow
    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return None

    # Use Tesseract to extract text from the image
    text = pytesseract.image_to_string(img)

    return text

def save_text_to_file(text, filename="output.txt"):
    with open(filename, "w") as file:
        file.write(text)

    print(f"Text saved to {filename}")

if __name__ == "__main__":
    # Get user input for image file path
    image_path = input("Enter the path to the image file: ")

    # Check if the file exists
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
    else:
        # Extract text from the image
        text = image_to_text(image_path)
        
        if text:
            # Output the extracted text
            print("\nExtracted Text:\n")
            print(text)

            # Optionally save the text to a file
            save_option = input("Do you want to save the extracted text to a file? (y/n): ")
            if save_option.lower() == 'y':
                save_text_to_file(text)
