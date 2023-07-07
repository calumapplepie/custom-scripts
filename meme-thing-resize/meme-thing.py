from wand.image import Image
from wand.color import Color
with Image(filename="./baseImage.jpg") as baseImage:
    with Image(width=baseImage.width, height=baseImage.height, background=Color("transparent")) as composite:
        newImage = baseImage.clone()
        newImage.transform(resize="50%x100")
        newImage.alpha_channel = True
        newImage.background_color= Color("transparent")
        newImage.extent(width=baseImage.width,height=baseImage.height,gravity="center")
        newImage.save(filename=img1.gif)

        """
        composite.image_set(newImage)
        newImage = baseImage.clone()
        newImage.transform(resize="100%x50")
        newImage.alpha_channel = True
        newImage.background_color= Color("transparent")
        newImage.extent(width=baseImage.width,height=baseImage.height,gravity="center")
        composite.image_add(newImage)
        composite.save(filename="final.gif") 
        """
