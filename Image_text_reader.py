from tkinter import filedialog
from tkinter import * #import all function from tkinter
import sys
import os
root = Tk()
root.title("Image to text converter by Miro 2021") #title of main window


def Browse_button():
    global directory #accesable from all functions but it should be replaced by class
    
    # Get the file location
    directory = filedialog.askopenfilename(initialdir = 'C:/Users/%s', 
                                            title = "Please select a file",
                                            filetypes =  (("All","*.png *.jpeg .*gif"),
                                                        ("png files","*.png"),
                                                        ("jpeg files","*.jpeg"),
                                                        ("gif files", ".gif")))
    print(directory)

def ImageToText():
    import cv2 #python wrapper
    import pytesseract #possible to use also PDF and so on - click one pytesseract
    
    global st #accesable from all functions but it should be replaced by class

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    
    image = cv2.imread(directory)

    st = pytesseract.image_to_string(image)

    print(st)    

def Save_file_as():
  
    f = filedialog.asksaveasfile(mode='w', title = "Save file as",
                                defaultextension ='*.txt',         #defaultextension is neccasary for saving with suffix (automaticaly)
                                filetypes = (("Word 97 - 2003", "*.doc"),
                                            ("Word 2007", "*.docx"),
                                            ("Text document", "*.txt")))

    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = st # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close() 

#GUI driver
if __name__ == "__main__":

    root.configure(background = 'light green')
    root.geometry("400x175")
    v = StringVar()
    button1 = Button(text = "Image Location: ", command = Browse_button).grid(row=0, column=3)
    button2 = Button(text = "Convert", command = ImageToText).grid(row=0, column=4)
    button3 = Button(text = "Save file as: ", command = Save_file_as,).grid(row=0, column=5)
    mainloop() 