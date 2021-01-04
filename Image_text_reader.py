from tkinter import filedialog
from tkinter import * #import all function from tkinter
import sys
import getpass
# Need this for the `os.path.split` function
import os
root = Tk("Miro")

if sys.version_info[0] < 3:
   import Tkinter as Tk
else:
   import tkinter as Tk


def Browse_button():
    global directory 
    # Get the file
    file = filedialog.askopenfilename(initialdir='C:/Users/%s')
    # Split the filepath to get the directory
    directory = os.path.split(file)[0]
    print(directory)

def ImageToText():
    import cv2
    import pytesseract #possible to use also PDF and so on - click one pytesseract
    
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    
    image = cv2.imread(directory)

    st = pytesseract.image_to_string(image)

    print(st)

#GUI driver
if __name__ == "__main__":

    root.configure(background = 'light green')
    root.geometry("400x175")
    v = StringVar()
    button1 = Button(text = "Image Location :", command = Browse_button).grid(row=0, column=3)
    button2 = Button(text = "Convert", command = ImageToText).grid(row=0, column=4)
    mainloop() 
