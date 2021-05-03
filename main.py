from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageChops
import sys
import math

def tolum(r,g,b):
	return (0.2126*r + 0.7152*g + 0.0722*b) 


if(len(sys.argv)!=3):
    sys.exit("Missing argument! [background] [bobber]")


background = Image.open(sys.argv[1])
image = Image.open(sys.argv[2])
outputimage = image
background = background.filter(ImageFilter.BoxBlur(1))
image = image.filter(ImageFilter.BoxBlur(1))

difference = ImageChops.subtract(image, background)
difference = difference.filter(ImageFilter.BoxBlur(2))

x2, y2 = difference.size
x = 0
y = 0

pixels = 0
count = 0
while(y<y2):
    while(x<x2):
        r,g,b = image.getpixel((x,y))
        pixels = pixels+tolum(r,g,b)
        count = count+1
        x=x+1
    y=y+1
    x=0

averagebrightness = pixels/count
	
x=0
y = 0
_left = x2
_right = 0
_top = y2
_bottom = 0
if(averagebrightness<40):
    averagebrightness=averagebrightness*2

while(y<y2):
    while(x<x2):
        r,g,b = difference.getpixel((x,y))
        if(tolum(r,g,b)>averagebrightness):
            #print(tolum(r,g,b))
            if(x<_left):
                _left = x
            if(x>_right):
                _right = x
            if(y<_top):
                _top = y
            if(y>_bottom):
                _bottom = y
            difference.putpixel((x,y), (0,255,0))
        x=x+1
    y=y+1
    x=0

if(_right +_bottom == 0):
	sys.exit("Not Found")

draw = ImageDraw.Draw(outputimage)
draw.rectangle((_left-10,_top-20,_right+10,_bottom+20),outline=(255,0,0))
outputimage.show()
outputimage.save('out.bmp')
inp = input()
sys.exit()