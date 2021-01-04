import numpy as np
import math

filename=0;

#im,height,width
class ImageFilt:
    
    def __init__(self,filename,im,height,width):
        self.filename = filename                           
        self.im = im
        self.height = height
        self.width = width
        print("im in init")
        
    def load_im(self,filenameame):
       # A method named load_im() that loads the image, sets height and width and
       #returns true if the file exists; else returns false and prints a warning that says
       #“Cannot find the image file”.
        try:
            f = open(filename)
            return True
            
        except:
            print("sa")
            
    def filter_im(f):
        #The method filter_im(f) that filters the image using a blur filter if f=0, or using a
        #sharpening filter if f =1.
        
    def plot_im():
        #The method plot_im() that plots the original and filtered images as subplots in a
        #single figure window.
        
   
                  