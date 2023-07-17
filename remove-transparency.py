import os
from PIL import Image
import sys

parametro = sys.argv
parametro.pop(0)

try:
    image = Image.open('%s_logo2.png' %parametro[0])
    
    if image.mode == 'RGBA':
        bg = Image.new('RGB', image.size, (255, 255, 255))
        bg.paste(image, (0, 0), image)
        bg.save("22345_logo2.png")

except:
    pass