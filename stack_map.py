#####STACK PROCESSED MAP#############
#To stack the maps (that have been processed to only contain the yellow pixels (or one day shipping))
#to become one whole map

import PIL
import PIL.Image
import numpy as np
import pandas as pd

# Put name of the maps (you have processed to only contain yellow pixels) in the variable zips
# Example:
# zips=['maps_0403.png', 'maps_0466.png', 'maps_1032.png', 'maps_0566.png', 'maps_1170.png', 'maps_0554.png', 'maps_0816.png', 'maps_0415.png', 'maps_0810.png', 'maps_0478.png', 'maps_0382.png', 'maps_0388.png', 'maps_0386.png', 'maps_0888.png', 'maps_1219.png', 'maps_1305.png', 'maps_1163.png', 'maps_0653.png', 'maps_0338.png', 'maps_1255.png']
zips=[]
# Put the number of maps in the variable STR
# Example:
# STR='20'
STR=''

top_zips = []

# Function to open images that has been converted
def get_img(i):
  try:
    img = PIL.Image.open("images_convert/" + zips[i]).convert('RGBA')
    return img
  except:
    return False

# Define range of color
base_img=None
colorup=np.array([255,235,124])
colordown=np.array([211,193,0])

# Function to stack the maps, where each overlapping yellow color will be redefined as green
def add_img(zip, img):
  width, height = img.size
  pix = img.load()
  count = 0
  overlap_count = 0
  b_pix = base_img.load()
  for x in range(width):
    for y in range(height):
      r,g,b,a= pix[x,y]
      if (r != 255 or g != 214 or b != 33) and (r != 0 or g != 0 or b != 0):
        pix[x, y] = (255, 255, 255, 0)
      if (r == 255 and g == 214 and b == 33):
        count += 1
        b_r, b_g, b_b, b_a = b_pix[x,y]
        if (b_g == g and b_b == b):
          b_pix[x, y] = (b_r - 50, g, b)
          overlap_count += 1
        else:
          b_pix[x,y] = (r, g, b)
  print(zip, "Count:", count, "Overlap:", overlap_count)
  if count >= 6000:
    top_zips.append((zip, count))

for i in range(0,1389):
  img = get_img(i)
  if img != False:
    width, height = img.size
    pix = img.load()
    count = 0
    if base_img == None:
      base_img = img
      for x in range(width):
        for y in range(height):
          r,g,b,a= pix[x,y]
          if (r != 255 or g != 214 or b != 33) and (r != 0 or g != 0 or b != 0):
            pix[x, y] = (255, 255, 255, 0)
          if (r == 255 and g == 214 and b == 33):
              count += 1
      print(i, ":", count-56)
    else:
      add_img(i, img)
      if count >= 6000:
        top_zips.append((i, count))
  else:
   print("Failed to open image of", i)


base_img.show()
base_img.save('overlap_'+STR+'.png')
print(top_zips)