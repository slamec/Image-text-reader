from tkinter import filedialog
from tkinter import * #import all function from tkinter
import tkinter.messagebox #message box
import sys
import os
root = Tk() #save file as .pyw to not open cmd window (for exe file use pyinstaller)
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

def Image_to_text():
    import cv2 #python wrapper
    import pytesseract #possible to use also PDF and so on - click one pytesseract

    
    global st #accesable from all functions but it should be replaced by class

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    
    image = cv2.imread(directory)

    st = pytesseract.image_to_string(image, lang='eng+ces', config='--psm 1')
    #important to get file with proper encoding

    print(st)

def Save_file_as():
  
    f = filedialog.asksaveasfile(mode='w', title = "Save file as",
                                defaultextension ='*.txt',         #defaultextension is neccasary for saving with suffix (automaticaly)
                                filetypes = (("Word 97 - 2003", "*.doc"),
                                            ("Word 2007", "*.docx"),
                                            ("Text document", "*.txt")))

    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = st 
    f.write(text2save) 
    f.close() 

def Message_window_convert():
   tkinter.messagebox.showinfo( "Done", "Your image is converted")  

def Message_window_save():
   tkinter.messagebox.showinfo("My task is done" ,"Your file has been saved, see you next time!")    

#GUI driver
if __name__ == "__main__":

    root.configure(background = 'light blue')
    root.geometry("380x170")
    v = StringVar()
    button1 = Button(width = 20, height = 3, text = "Image Location: ", command = Browse_button).grid(row=0, column=2)
    #lamda needs to be used to call more commands via one Button
    button2 = Button(width = 20, height = 3, text = "Convert", command = lambda:[Image_to_text(),Message_window_convert()]).grid(row=1, column=2)
    button3 = Button(width = 20, height = 3, text = "Save file as: ", command = lambda: [Save_file_as(),Message_window_save()]).grid(row=2, column=2) 
    root.mainloop() 
