from tkinter import * #import all function from tkinter
root = Tk("Miro") #GUI window

variable1 = StringVar(root)
variable2 = StringVar(root) #create a global variable

variable1.set("Image location") #
variable2.set("Location to save image") #


def ImageToText():
    import cv2
    import pytesseract #possible to use also PDF and so on - click one pytesseract
    import json
    

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    image = AskForFileLocation 

    st = pytesseract.image_to_string(image)

    create_file = open

     

