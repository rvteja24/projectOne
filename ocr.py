try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import inputMain
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
print("Serving your speech hot!")
textContent = (pytesseract.image_to_string(Image.open(inputMain.inputVal)))
print(textContent)