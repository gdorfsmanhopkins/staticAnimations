import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#Chimera expects white images on a black background
plt.style.use('dark_background')
plt.figure(figsize=(6,6)) #Size frame to 8"x8" to match our printer's build plate

NUM_PTS = 1000 #Sample points for the drawn curve, more is smoother
NUM_FRAMES = 161 #Number of frames in the animation

theta = np.linspace(0, 2*np.pi, NUM_PTS)

#Each loop makes a frame
for i in range(NUM_FRAMES):
    t = 0.2 + .005*i
    r = 2 + t*np.cos(5*theta + 2*np.pi*t) #The curve's the defining function
    plt.polar(theta,r,alpha=0) #Draws the curve transparently
    plt.fill_between(theta,0,r,color='white') #Fills the curve in white
    plt.axis('off') #Removes axes, we just want the flower

    #Now export and clear the plot.
    imageName = 'flowerStack/flowers_'+str(1000+i)+'.png'
    plt.savefig(imageName)
    plt.cla()

#Chimera doesn't like alpha layers...we must remove them
#For this import each image in your stack and remove the alpha layer

for i in range(NUM_FRAMES):
    in_name = 'flowerStack/flowers_'+str(1000+i)+'.png'
    out_name = 'flowerStack/flowers_'+str(1000+i)+'.png'
    image = Image.open(in_name).convert('RGB') #This is the conversion step!
    image.save(out_name)
