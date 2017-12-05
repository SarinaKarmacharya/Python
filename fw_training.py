# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 11:11:32 2017

@author: vs796
"""

from medpy.io import load
from medpy.io import header
import matplotlib.pyplot as plt
import numpy as np



image_data, image_header = load('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/MSD/case201_MSD.nii')
print (image_data.shape)
N = image_data.shape[2]
print(header.get_pixel_spacing(image_header))


#path = '/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/MSD/case117_MSD.nii'


axial_middle = image_data.shape[2] / 2





new_image_data = np.multiply(axial_middle, 2)


for x in range(1, 74):
    axial_middle = x
    plt.figure('Showing the datasets')
    plt.subplot(1, 2, 1).set_axis_off()
    plt.imshow(image_data[:, :, axial_middle].T, cmap='gray', origin='lower')
    plt.show()