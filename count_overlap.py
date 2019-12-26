#####COUNT OVERLAP AREA#############
# To count the number of overlap pixel (represented by greens)

import PIL
import PIL.Image
import numpy as np
import pandas as pd

# Put name of the overlap maps you have processed in the variable zips
# Example for 1 overlap map
# zips=['overlap_9.png']
# Example for multiple overlap maps
# zips=['overlap_9.png','overlap_10.png','overlap_11.png', 'overlap_12.png', 'overlap_13.png','overlap_14.png','overlap_15.png', 'overlap_20.png','overlap_25.png','overlap_30.png']
zips=[]

# Function to count the overlap areas
# Counting all pixels except the yellow (representing one day shipping without overlap) and black (the borders or outlines)
def count_overlap(zip):
    count=0
    img = PIL.Image.open(zip).convert("RGBA")
    w, h = img.size
    pix = img.load()
    for x in range(w):
        for y in range(h):
            r, g, b, a = pix[x, y]
            if (r,g,b)!=(255,214,33) and (r,g,b)!=(0,0,0) and a!=0:
                count += 1
    print(zip, "overlap", count/301664)
    
for zip in zips:
    count_overlap(zip)
