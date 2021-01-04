
import cv2
import pytesseract #possible to use also PDF and so on - click one pytesseract
    
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

image = cv2.imread(input("Please insert file path or name :"))
    
st = pytesseract.image_to_string(image)

print(st)