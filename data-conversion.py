""" data-conversion.py  |  Thomas Pasfield  |  1-20-2024
    Converts TIFF format image data into Numpy matrices. Allows easy
    export to new files.

    !! NOT NEEDED IF YOU HAVE ACCESS TO THE TEAM DRIVE. MATRIX FILES 
    ARE PROVIDED IN THAT LOCATION. !!

    May turn this into a module later if needed, but will likely
    stay monolithic.

    If libtiff is not present, it can be installed through: 
        `pip install pylibtiff`
    If errors occur, verify that you have Microsoft Visual C++ Build
    Tools installed. (7 GB install.)

    Requires numpy, libtiff.
"""

import numpy as np
from libtiff import TIFF


# Initial full precision conversion to Numpy
x,y,z = 1085, 1085, 1789
img = np.zeros([x,y,z], dtype=np.float32)
for i in range(z):  # Iterate through all images and load them
    # Ensure that the stack folder is within the repository. You must add it yourself.
    tif = TIFF.open(r"./2024_REU_PNNL/3DprintA_downx2_" + str(i) + ".tif", mode='r')
    img[:,:,i] = tif.read_image()

# Save matrix to .npy format.
np.save("./2024_FULL-STACK.npy", img)


"""
Reduced precision conversion. Useful for smaller file sizes and
application where qualitative properties are more valuable than
quantitative.

Data is truncated and normalized to a smaller range of values 
that contain the object. This allows more information to be
preserved in the reduced precision.
"""

reduced_img = img - 9600
reduced_img[reduced_img<0] = 0  # Removes nonnegative values, sets to zero.
reduced_img = reduced_img / np.max(reduced_img)  # Normalize to [0,1]
reduced_img = reduced_img * 255  # Scale to unsigned 8 bit integers
reduced_img = np.array(reduced_img, dtype=np.uint8)  # Convert type to uint8

np.save("./NORMALIZED-RP-STACK.npy", reduced_img)