################PROCESS MAP PIXEL###########################
# Store only the yellow pixels in a map
import PIL
import PIL.Image
import os

top_zips = []

# Set directory of original image
for file_name in os.listdir("images_conv/"):
    top_zips.append(file_name)
    
zips=top_zips
    
# Function that convert image only to store yellow pixels
def conv_img(zip):
    img = PIL.Image.open("images/" + zip).convert("RGBA")
    w, h = img.size
    pix = img.load()
    for x in range(w):
        for y in range(h):
            r, g, b, a = pix[x, y]
            if (r != 255 or g != 214 or b != 33) and (r != 0
               or g != 0 or b != 0):
                pix[x, y] = (255, 255, 255, 0)
    img.save("images_conv/" + zip)
    return img
    
for i in range(len(zips)):
    conv_img(zips[i])