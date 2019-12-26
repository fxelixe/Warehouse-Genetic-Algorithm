#####COUNT TOTAL OF PIXEL#############
# Count number of pixel in a map
import PIL
import PIL.Image

count=0
# Load any map
img = PIL.Image.open('maps_0003.png').convert("RGBA")
w, h = img.size
pix = img.load()
for x in range(w):
    for y in range(h):
        r, g, b, a = pix[x, y]
        if (a!=0) and (r,g,b)!=(0,0,0) :
            count+=1

# Total number of pixels is 301664