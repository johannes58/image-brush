"""MODULE images2gif

Provides a function (writeGif) to write animated gif from a series of PIL images or numpy arrays.

This code is provided as is, and is free to use for all.

Almar Klein (June 2009)

-based on gifmaker (in the scripts folder of the source distribution of PIL)
-based on gif file structure as provided by wikipedia

"""

try:
    import PIL
    from PIL import Image, ImageChops
    from PIL.GifImagePlugin import getheader, getdata
except ImportError:
    PIL = None

try:
    import numpy as np
except ImportError:
    np = None

# getheader gives a 87a header and a color palette (two elements in a list).
# getdata()[0] gives the Image Descriptor up to (including) "LZW min code size".
# getdatas()[1:] is the image data itself in chuncks of 256 bytes (well
# technically the first byte says how many bytes follow, after which that
# amount (max 255) follows).



def intToBin(i):
    """ Integer to two bytes """
    # devide in two parts (bytes)