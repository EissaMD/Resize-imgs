from PIL import Image
import os
from os import listdir
import tkinter as tk
from tkinter.ttk import *

class App(tk.Tk):
    WIDTH = 400
    HEIGHT = 360
    def __init__(self):
        super().__init__()
        self.title("Resize Images")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.minsize(App.WIDTH , App.HEIGHT)
        self.maxsize(App.WIDTH , App.HEIGHT)
        self.grid_columnconfigure(0, weight=1)
        # title
        Label(self,text="Resize Images" , font="Times 25 bold").grid(row=0, column=0, pady=20 )
        # ask for folder path
        path_frame = Frame(self)
        path_frame.grid(row=1, column=0 , sticky = "we")
        path_frame.columnconfigure((0,2),weight=1 )
        path_frame.columnconfigure(1,weight=10)
        Label(path_frame,text=f"File Path :" ).grid(row=0, column=0,  sticky = "we" , padx=(5,0) , pady=10 )
        path_entry = Entry(path_frame)
        path_entry.grid(row=0, column=1,sticky="we")
        Button(path_frame, text="Select Folder").grid(row=0, column=2 , padx=(0,5))
        # ask for image dimensions
        dimensions_frame = Frame(self)
        dimensions_frame.grid(row=2, column=0 , sticky = "we")
        Label(dimensions_frame,text=f"Image size :  " ).pack(side="left")
        entry_w = Entry(dimensions_frame , width=10)
        entry_w.pack(side="left")
        Label(dimensions_frame,text=f"X" ).pack(side="left")
        entry_h = Entry(dimensions_frame , width=10)
        entry_h.pack(side="left")
        # show image names in a text box
        textbox = tk.Text(self , bg="gray90" , height=10)
        textbox.grid(row=3, column=0 ,sticky="nswe" , pady=10, padx=10)
        Button(self, text="Re-size").grid(row=4, column=0 )
        
def resize():    
    imgs_path = r"."
    img_size = (200 , 200)

    output_folder = imgs_path+r"\output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # get the path or directory
    for img_name in os.listdir(imgs_path):
        # check if the image end swith png or jpg or jpeg
        if img_name.endswith(".png") or img_name.endswith(".jpg"):
            image = Image.open(imgs_path+"\\"+img_name)
            new_image = image.resize(img_size)
            new_image.save(output_folder+"\\"+img_name)


if __name__ == "__main__":
    app = App()
    app.mainloop()