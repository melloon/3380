import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk,Image  
from datetime import date
from datetime import datetime

fileName = ""

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.frameMain = Frame(self)
        self.frameMain.grid(row=0, column=0)
        self.frameCanvas = Frame(self)
        self.frameCanvas.grid(row=1, column=0)
        self.frameDetails = Frame(self)
        self.frameDetails.grid(row=2, column=0)
        

        # set window title
        self.winfo_toplevel().title("Image Hashing Program")



        # create widgets
        # label
        self.uploadLabel = ttk.Label(self.frameMain, text=' ', wraplength=500)
        self.uploadLabel.grid(row=1, column=1)
        # upload photo button
        self.uploadPhoto_button = ttk.Button(self.frameMain, text='Choose Photo', width=30, command=self.browseFiles)
        self.uploadPhoto_button.grid(row=2, column=1, padx=5)
        
        # hashify button
        self.hashify_button = ttk.Button(self.frameMain, text='Hashify', width=30, command=self.hashify_button_clicked, state=DISABLED)
        self.hashify_button.grid(row=3, column=1, padx=5)
        # hashify status label
        self.hashifyStatusLabel = ttk.Label(self.frameMain, text=' ')
        self.hashifyStatusLabel.grid(row=4, column=1, padx=5, pady=5)



        # create empty preview canvas
        self.previewCanvas = tk.Canvas(self.frameCanvas, bg='grey', width=600,height=350)
        self.previewCanvas.grid(row=4,column=2,pady=30)
        #  create empty image
        self.displayPreviewImage = ttk.Label(self.frameCanvas)


         
        # FUNCTIONS

        # set the controller
        self.Controller = None
    def set_controller(self, controller):
        self.Controller = controller

        # hashify button
    def hashify_button_clicked(self):
        self.Controller.SendFile(self.fileName)
        # <Insert Hash Call>
        
        # Get matchfound result and replace the "false" below
        if(False):
            # Match Found
            self.hashifyStatusLabel.configure(text="Image has been hashed. Match found!")
        
        else:
            # Match Not Found
            self.hashifyStatusLabel.configure(text="Image has been hashed. No match found, please add additional information below.")
            self.hashify_button['state'] = DISABLED
        
            # ACTIVATE INFORMATION SECTION
            # file details
            # name
            self.imageName = ttk.Label(self.frameDetails, text="Image Name: ")
            self.imageName.grid(row=1, column=1, padx=5, sticky='w')
            self.imageNameInput = tk.Text(self.frameDetails, height=1, width=25)
            self.imageNameInput.grid(row=1, column=2, padx=5, pady=5)
            # date
            self.imageDate = ttk.Label(self.frameDetails, text="Date:")
            self.imageDate.grid(row=2, column=1, padx=5, sticky='w')
            self.imageDateLabel = ttk.Label(self.frameDetails, text=date.today().strftime("%m/%d/%y"))
            self.imageDateLabel.grid(row=2, column=2, padx=5, pady=5, sticky='w')
            self.outDate = date.today().strftime("%m/%d/%y")
            # time
            self.imageTime = ttk.Label(self.frameDetails, text="Time:")
            self.imageTime.grid(row=3, column=1, padx=5, sticky='w')
            self.imageTimeLabel = ttk.Label(self.frameDetails, text=datetime.now().strftime("%H:%M:%S"))
            self.imageTimeLabel.grid(row=3, column=2, padx=5, pady=5, sticky='w')
            self.outTime = datetime.now().strftime("%H:%M:%S")
            # description
            self.imageDescription = ttk.Label(self.frameDetails, text="Description:")
            self.imageDescription.grid(row=4, column=1, padx=5, sticky='nw')
            self.imageDescriptionInput = tk.Text(self.frameDetails, height=6, width=25)
            self.imageDescriptionInput.grid(row=4, column=2, padx=5, pady=5)
        
            # Append new info button
            self.appendInfo_button = ttk.Button(self.frameDetails, text='Append New Info', width=30, command=self.appendInfo_button_clicked)
            self.appendInfo_button.grid(row=5, column=2, padx=5, pady=5)
            # Append new info label
            self.appendInfoLabel = ttk.Label(self.frameDetails, text=' ', wraplength=400)
            self.appendInfoLabel.grid(row=6, column=2, padx=5, pady=5)



       

    def appendInfo_button_clicked(self):
        # output txt file generation
        self.outName = self.imageNameInput.get(1.0, "end-1c")
        self.outDes = self.imageDescriptionInput.get(1.0, "end-1c")
        OutputString = "Image Name: {}\nDate: {}\nTime: {}\nDescription: {}".format(self.outName, self.outDate, self.outTime, self.outDes)
        with open('detailOut.txt', 'w') as f:
            f.write(OutputString)

        self.appendInfoLabel.configure(text="Information Added!")
        self.appendInfo_button['state'] = DISABLED
            
            

    def browseFiles(self):
        # open file browser
        self.fileName = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = (("Text files",
                                                            "*.jpg*"),
                                                           ("all files",
                                                            "*.*")))
        shortFilename = self.fileName[0:10] + "..." + self.fileName[-4:]
        
        # change label contents
        self.uploadLabel.configure(text="File Opened: " + shortFilename)
        
        # enable buttons
        self.hashify_button['state'] = NORMAL
        

        # open image
        self.img = Image.open(self.fileName)
        # resize image
        hpercent = (300 / float(self.img.size[1]))
        wsize = int((float(self.img.size[0]) * float(hpercent)))
        self.img = self.img.resize((wsize, 300), Image.ANTIALIAS)
        # display image
        self.previewImage = ImageTk.PhotoImage(self.img)
        self.displayPreviewImage.config(text='Image Preview', width=100, image=self.previewImage)
        self.displayPreviewImage.image = self.previewImage
        self.displayPreviewImage.grid(row=4, column=2, pady=30)

        


        
