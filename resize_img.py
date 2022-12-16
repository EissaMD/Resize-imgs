from PIL import Image
import os
from os import listdir
import tkinter
from tkinter.ttk import *

class App(tkinter.Tk):
    WIDTH = 400
    HEIGHT = 500
    def __init__(self):
        super().__init__()
        self.title("Data Editor")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.minsize(App.WIDTH , App.HEIGHT)
        self.maxsize(App.WIDTH , App.HEIGHT)
        self.grid_rowconfigure(0, weight=1)
        
        
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