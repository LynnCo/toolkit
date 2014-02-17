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
    images2gif.py [included]
    matplotlib
    numpy
'''
import time
import numpy
import PIL
import matplotlib
import matplotlib.pyplot
import os
import images2gif

def visualize(display):
    '''
    display: = "gif" or "png" or "plot"
    '''
    matplotlib.pyplot.ion()
    npframes = numpy.load("output.npy")
    xs = range(npframes[0].shape[0]+1)
    ys = range(npframes[0].shape[1]+1)
    X,Y = numpy.meshgrid(xs,ys)
    dataList = matplotlib.pyplot.pcolormesh(X,Y,npframes[0],cmap="hot")
    images = list()
    for i in range(1,len(npframes)):
        thisFig = "figure"+str(i)+".png"
        dataList.set_array(npframes[i].ravel())
        dataList.autoscale()
        if display == ("png" or "gif"):
            matplotlib.pyplot.savefig(thisFig)
        if display == "gif":
            images.append(PIL.Image.open(thisFig))
            os.remove(thisFig)
        if display == "plot":
            matplotlib.pyplot.draw()
            time.sleep(0.025)
    if display == "gif":
        animName = "output_gif.gif"
        images2gif.writeGif(filename=animName, images=images, duration=0.1, repeat=True)
    print("visualization successful")
    return

if __name__ == "__main__":
    visualize()