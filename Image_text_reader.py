from tkinter import * #import all function from tkinter
root = Tk("Miro") #GUI window

variable1 = StringVar(root)
variable2 = StringVar(root) #create a global variable

variable1.set("currency") #
variable2.set("currency") #


def AskForFileLocation():

   input = filedialog.askopenfile(initialdir="/")
   print(input)
   for i in input:
      print(i)

      x = Button(base, text ='Select a .txt/.csv file', command = lambda:file_opener())
x.pack()
mainloop()


def ImageToText():
    import cv2
    import pytesseract #possible to use also PDF and so on - click one pytesseract
    import json
    

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    image = AskForFileLocation 

    st = pytesseract.image_to_string(image)

    create_file = open

     

