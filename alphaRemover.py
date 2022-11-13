#Chimera doesn't like alpha layers...we must remove them
#This imports each image in your stack and removes the alpha layer

from PIL import Image

NUM_FRAMES = 161 #Set this to the number of frames you wish to convert

for i in range(NUM_FRAMES):
    #The names must be adjusted to correctly grab your image stack
    #Currently it saves the processed files to a new folder rather than overwriting
    in_name = 'flowerStack/flowers_'+str(1000+i)+'.png'
    out_name = 'flowerStackProcessed/flowers_'+str(1000+i)+'.png'

    image = Image.open(in_name).convert('RGB') #This is the conversion step!
    image.save(out_name)
