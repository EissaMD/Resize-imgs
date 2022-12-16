from PIL import Image
import os
from os import listdir

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