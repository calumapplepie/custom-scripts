from wand.image import Image
from wand.color import Color
import math
from math import sin, cos
numFrames = 20
with Image(filename="./newBase.png") as baseImage:
    with Image(width=baseImage.width, height=baseImage.height, background=Color("transparent")) as composite:
        composite.image_remove()
        for i in range(0,numFrames):
            newImage = baseImage.clone()
            resize_width = 25*(1+sin(i/numFrames*2*math.pi))+50
            resize_height = 25*(1+cos(i/numFrames*2*math.pi))+50
            resize_str = "{0}%x{1}".format(resize_width, resize_height)
            print(resize_str)
            newImage.transform(resize=resize_str)
            newImage.alpha_channel = True
            newImage.background_color= Color("transparent")
            newImage.extent(width=baseImage.width,height=baseImage.height,gravity="center")
            newImage.dispose = "background"
            newImage.background_color = "transparent"
            newImage.delay = 1
            composite.image_add(newImage)
        composite.save(filename="final.gif") 
