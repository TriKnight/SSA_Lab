# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:26:44 2023

@author: HP
"""

import numpy as np
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.utils.image_utils import array_to_img, img_to_array, load_img
import cv2
import glob

datagen = ImageDataGenerator(rotation_range =40, 
                         width_shift_range = 0.2, 
                         height_shift_range = 0.2,
                         shear_range=0.2, 
                         zoom_range=0.2, 
                         horizontal_flip = True, 
                         fill_mode = 'nearest')

file = r"C:\Users\HP\Documents\Aug\*.jpg"
glob.glob(file)
images = [cv2.imread(image) for image in glob.glob(file)]
print(images)
for img in images:
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)
    
    i = 0
    for batch in datagen.flow (x, batch_size=1, save_to_dir =r'C:\Users\HP\Documents\Aug', save_prefix ='people2', save_format='jpg'):
        i+=1
        if i > 10:
            break