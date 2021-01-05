import numpy as np
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
import PIL
import cv2
from PIL import Image, ImageFilter

#,im,height,width
class ImageFilt:
    def __init__(self,filename):
        self.filename = filename                           
        self.im = 0
        self.height = 0
        self.width = 0
    
    def load_im(self):

        try: 
            self.im = cv2.imread(self.filename)
            #print(self.im)
            self.height, self.width, channels = self.im.shape
            print("width of image",self.width)
            print("height of image",self.height)
            return True
        
        except:
            print("Cannot find the image file")
          
                    
    def filter_im(self,f):
        #The method filter_im(f) that filters the image using a blur filter if f=0, or using a
        #sharpening filter if f =1.
        if f==1:
            kernel = np.ones((5,5),np.float32)/25
            dst = cv2.filter2D(self.im,-1,kernel)

            plt.subplot(121),plt.imshow(self.im),plt.title('Original')
            plt.xticks([]), plt.yticks([])
            plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
            plt.xticks([]), plt.yticks([])
            plt.show()
            
        elif f==0:
            pass
        
    def plot_im():
        #The method plot_im() that plots the original and filtered images as subplots in a
        #single figure window.
        pass
        
        
path = '/home/hk/Desktop/bionluk/sa.jpeg'
image = ImageFilt(path)
image.load_im()
image.filter_im(1)

