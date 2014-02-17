'''
visualize.py

Used to visualize numpy data sets

Use
    python visualize.py gif
    python visualize.py png
    python visualize.py plot

Dependencies
    Python 2.7
    PIL
    matplotlib
    numpy
    images2gif.py
'''

import time
import numpy
import PIL
import matplotlib
import matplotlib.pyplot
import matplotlib.pyplot as plt
import os
import sys
import images2gif

def visualize(display):
    plt.ion()
    npframes = numpy.load("data/output.npy")
    xs = range(npframes[0].shape[0]+1)
    ys = range(npframes[0].shape[1]+1)
    X,Y = numpy.meshgrid(xs,ys)
    dataList = plt.pcolormesh(X,Y,npframes[0],cmap="hot")
    images = list()
    for i in range(1,len(npframes)):
        thisFig = "img/figure"+str(i)+".jpg"
        dataList.set_array(npframes[i].ravel())
        dataList.autoscale()
        if display == "gif":
            plt.savefig(thisFig)
            images.append(PIL.Image.open(thisFig))
            os.remove(thisFig)
        elif display == "png":
            plt.savefig(thisFig)
        elif display == "plot":
            plt.draw()
            time.sleep(0.025)
        else:
            print("invalid display")
            return "False"
    if display == "gif":
        animName = "img/plot_gif.gif"
        images2gif.writeGif(filename=animName, images=images, duration=0.1, repeat=True)
    print("visualization successful")
    return "True"

if __name__ == "__main__":
    visualize(sys.argv[1]) 