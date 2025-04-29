#! python

import numpy as np
from bin_char import *

tstr = '十月一日西環臨時炒車'
spacing = 1
bstr = ()

for c in tstr:
    bstr +=tuple([np.zeros([24,spacing])])
    bstr +=tuple([bin_char(c)])
    bstr +=tuple([np.zeros([24,spacing])])
bstrmap = np.hstack(bstr)

from PIL import Image

# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.new( 'RGB', bstrmap.shape[::-1], "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every col:
    for j in range(img.size[1]):    # For every row
        col = np.array([255,192,0])
        outp = bstrmap[j,i]*col
        pixels[i,j] = tuple(int(x) for x in outp) # set the colour accordingly
# img.show()
img.save("test.png")