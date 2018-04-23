##
# Part 1
# Worksheet 1 exercises for learning module 28 Images

# 1 	Problem 
# Using functions from the scipy package, 
# load the image bird.jpg from the data section of the course. 
# In Chapter 15 of the textbook, code was presented that enabled you to isolate the elements of a matrix of distance 10 from a central point. Since an image is just a matrix, create a filter that isolates the pixels around the birds head in the image. You will have to provide a best guess as to where the center of the birds head is.  Save this as a new image, where only the birds head appears, perhaps in a circle or square, and everything else in the image is black. 

import scipy.misc as sm
import numpy as np
from PIL import Image, ImageOps, ImageDraw
def parrot_head():
    # mask = Image.open("bird.jpg").convert("L")
    im = Image.open("bird.jpg")
    im = im.crop((200,60,320,180))
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    im.putalpha(mask)

    output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save('output.png')

# 2 	Problem 
# Create a new image from bird.jpg by 
# swapping the color channels. 
# To accomplish this, the pixel values for the green channel were placed in the red channel, the pixel values for the blue channel were placed in the green channel, and the original pixel values for the red channel were placed in the blue channel. Things that were red in the original are blue in the output. 
def colorswap():
    import scipy.misc as sm
    img = sm.imread("bird.jpg")
    red = img[:,:,0].copy()
    green = img[:,:,1].copy()
    blue = img[:,:,2].copy()
    img[:,:,0]=green
    img[:,:,1]=blue
    img[:,:,2]=red
    sm.imsave("colorswap.png", img)
# colorswap()

##
# Part 2
# Worksheet 1 and 2 exercises for learning module 30 Py Random

# Worksheet 1
# 1	Problem 
# Generate two sets of random numbers from two different normal distributions. 
# A normal distribution is often denoted by its 
# parameters, mean shown as 𝜇 and standard deviation shown as 𝜎, and represented as 𝒩(𝜇, 𝜎) 
# The first distribution should have parameters (2,3). 
# The second distribution should have parameters (1,0.05). 
# Generate histograms for each distribution and plot them in the same graph. 
import math
def histooo():
    n = 300
    normaldist1 = np.random.normal(2, 3, n)
    normaldist2 = np.random.normal(1, 0.05, n)
    hist1 = np.histogram(normaldist1, bins=[-math.inf, -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, math.inf], range=(min(normaldist1), max(normaldist1)))
    hist2 = np.histogram(normaldist2, bins=[-math.inf, -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, math.inf], range=(min(normaldist2), max(normaldist2)))
    print("hist1")
    for key, value in zip(hist1[0], hist1[1]):
        print("{}, {}".format(key,value))
    print("hist2")
    for key, value in zip(hist2[0], hist2[1]):
        print("{}, {}".format(key,value))

# 2	Problem 
# Using the same seed, generate two vectors of random integers that are the same length. Subtract one vector from the other to confirm that the sequences are the same. 
def arr2():
    arr1 = np.random.rand(9)
    arr2 = np.random.rand(9)
    print(arr2-arr1)


# Worksheet 2 
 
# 1	Problem 
# Generate a sequence of DNA that is 100 bases long 
# using random integers 
# as in the video example.  
def foogihab():
    abet = ('A', 'C', 'G', 'T')
    nms = np.random.randint(0,4,100)
    dnalist = np.take(abet,nms)
    print("".join(dnalist))

# 2	Problem 
# In the second video, the code is presented to generate a deck of cards. 
# Add your own code to deal the deck to four players. 
# You will have to ensure that only one card is uniquely dealt to a single player. 
# Hint: investigate the options in numpy.random.choice() to sample your deck of cards without replacement. 
nos = "A 2 3 4 5 6 7 8 9 10 J Q K".split(" ")
suits = ['spades', 'diamonds','clubs','hearts']
cards = []
for i in nos:
    for j in suits:
        cards.append(i + ' ' + j)
for i in "1234":
    print("player "+i)
    deck = []
    for car in cards:
        deck.append(np.random.choice(cards, replace=False))
    print(deck)