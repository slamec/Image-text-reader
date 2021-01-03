from tkinter import filedialog
from tkinter import * #import all function from tkinter
import sys
root = Tk("Miro")

if sys.version_info[0] < 3:
   import Tkinter as Tk
else:
   import tkinter as Tk


def browse_button():
    filename = filedialog.askopenfile()

def ImageToText():
    import cv2
    import pytesseract #possible to use also PDF and so on - click one pytesseract
    
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    image = cv2.imread(browse_button) 

    st = pytesseract.image_to_string(image)

    print(st)

root.configure(background = 'light green')
root.geometry("400x175")
v = StringVar()
button1 = Button(text = "Image Location :", command=browse_button).grid(row=0, column=3)
button2 = Button(text = "Convert", command =ImageToText).grid(row=0, column=4)
mainloop() 
