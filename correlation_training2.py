# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:27:50 2017

@author: vs796
"""

import matplotlib.pyplot as plt
from medpy.io import load
import numpy as np
from scipy import signal
from scipy.stats.stats import pearsonr


image_data_msd, image_header_msd = load('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/MSD/case104_MSD.nii')
image_data_fw, image_header_fw = load('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/FW/case104_FW.nii')



axial_middle = 54
plt.figure('Showing the datasets')
plt.subplot(1, 2, 1).set_axis_off()
plt.imshow(image_data_fw[:, :, axial_middle].T, cmap='gray', origin='lower')
a = plt.show()


axial_middle = 35
plt.figure('Showing the datasets')
plt.subplot(1, 2, 1).set_axis_off()
plt.imshow(image_data_msd[:, :, axial_middle].T, cmap='gray', origin='lower')
b = plt.show()


print signal.correlate2d (a, b)

print pearsonr(np.any(image_data_msd), np.any(image_data_fw))