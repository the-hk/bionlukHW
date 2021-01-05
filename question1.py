import numpy as np
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
import cv2
import PIL



class ImageFilt:
    def __init__(self,filename,im=0,height=0,width=0,a=0):
        self.filename = filename                           
        self.im = im
        self.height = height
        self.width = width
        self.a=a
        self.blur = None
        self.sharp = None
    
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
            self.a=1
            self.blur = cv2.blur(self.im,(3,3))
            # plt.subplot(121),plt.imshow(self.im),plt.title('Original')
            # plt.xticks([]), plt.yticks([])
            # plt.subplot(122),plt.imshow(self.blur),plt.title('Averaging')
            # plt.xticks([]), plt.yticks([])
            # plt.show()
        elif f==0:
            self.a=0
            filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            self.sharp = cv2.filter2D(self.im,-1,filter)
            
            # cv2.imshow('Main', self.im)
            cv2.imshow("sharpened", self.sharp)
            
            cv2.waitKey(3000)
            cv2.destroyAllWindows()
            
            # filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            # self.sharpen = cv2.filter2D(self.im,-1,filter)
           
           
           
            
           
        
    def plot_im(self):
        #The method plot_im() that plots the original and filtered images as subplots in a
        #single figure window.,
        
        # plt.subplot(1, 3, 1), plt.imshow(self.im, 'gray'),plt.title("original")
        # plt.subplot(1, 3, 2), plt.imshow(self.blur, 'gray'),plt.title("blur")
        # cv2.imshow(self.sharp, 'sharp')
        # plt.savefig('final_image_name.extension') # To save figure
        # plt.show() 
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # final_frame = cv2.hconcat(self.blur, self.sharp)
        # cv2.imshow('picture', final_frame)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # cv2.imshow("selam",self.sharp)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        plt.subplot(121),plt.imshow(self.im),plt.title('original')
        plt.xticks([]), plt.yticks([])
        if self.a==1:
            plt.subplot(122),plt.imshow(self.blur),plt.title('blur')
            plt.xticks([]), plt.yticks([])
        if self.a==0:
            plt.subplot(122),plt.imshow(self.im),plt.title('sharpened')
            plt.xticks([]), plt.yticks([])
            
        # plt.subplot(133),plt.imshow(self.sharp),plt.title('sharpen')
        # plt.xticks([]), plt.yticks([])
        plt.show()        
       
        
        
    
        
        
path = '/home/hk/Desktop/bionluk/sa.jpeg'
image = ImageFilt(path)
image.load_im()
image.filter_im(0)
image.plot_im()


