###################GENETIC ALGORITHM #######################
#Processing the maps using genetic algorithm
import PIL
import PIL.Image
import os
import pyperclip
import random
import pandas as pd
import numpy as np
import matplotlib


top_zips = []

#set directory of processed images
for file_name in os.listdir("images_convert/"):
    top_zips.append(file_name)

zips=top_zips
    
    
#Constants
# Amount of Warehouses
QTY = 12 
STR = '12'
# Amount of Warehouse Location Sets per Generation
POP = 10  
# Amount of iterations
ITER = 1000  
# Total number of pixels in the UPS map (excluding Alaska, Hawaii, P.R., and border pixels)
TOTAL_PIXELS = 301664 
# Color of one-day delivery zone which is yellow
COLOR = (255, 214, 33,255)  


# Function that generates a beginning list of 50 zip codes
def gen_random_zips(q): #q=QTY
    random_zips = []
    for j in range(q):
        zip = top_zips[random.randint(0, len(top_zips) - 1)]
        i = np.array(zip)
        random_zips.append(zip)
    return random_zips

# Function that retrieves the UPS delivery time map given the zip code
def get_img(zip):
    img = PIL.Image.open("images_conv/" + zip)
    return img


# Function that counts the number of times a certain color occurs in an image
def count_color(img, color):
    colors = img.getcolors()
    pixels = None
    for tup in colors:
        if tup[1] == color:
            return tup[0]

for i in range(len(zips)):
    img = get_img(zips[i])
    if type(img)==None:
        print(zips[i])
        

# Function that determines the 'fitness' of a set of warehouse locations(a.k.a.its efficiency) as a float between 0. and 1.
def fitness(zips, show=False):
    comb_img = get_img(zips[0]).copy()
    #comb_img = pyperclip.copy(get_img(zips[0]))
    for i in range(len(zips)):
        img = get_img(zips[i]).convert("RGBA")
        [x,y]=img.size
        comb_img.paste(img, (0,0), img)
    if show == True:
        comb_img.show()
        comb_img.save('warehouse_'+STR+'.png')
    filled_pixels = count_color(comb_img, COLOR)
    #filled_pixels -= count_color(comb_img.crop((466, 213, 545, 352)), COLOR)
    # print("Filled pixels:", filled_pixels)
    del comb_img
    return filled_pixels / TOTAL_PIXELS

# Function that clones an array
def clone(array):
    new_array = []
    for elem in array:
        new_array.append(elem)
    return new_array


# Function that replaces one zip code with another random one.
def mutate(zips):
    new_zips = clone(zips)
    ind = random.randint(0, len(new_zips) - 1)
    new_zips[ind] = gen_random_zips(1)[0]
    return new_zips


gen = []
for i in range(POP):
    gen.append(gen_random_zips(QTY))

for i in range(ITER):
    gen = sorted(gen, key=fitness, reverse=True)
    print("Generation:", i, "Best:", fitness(gen[0]))
    for j in range(2, POP, 1):
        gen[j] = mutate(gen[j%2])

print("FINAL BEST:", fitness(gen[0], show=True))
print(gen[0])
