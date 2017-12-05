# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:38:25 2017

@author: vs796
"""


from medpy.io import load
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr


image_data_fs, image_header_fs = load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/freesurferINdwi/case104_wmparc-in-bse.nii.gz")
image_data_msd, image_header_msd = load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/MSD/case104_MSD.nii")
image_data_fw, image_header_fw = load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/FW/case104_FW.nii")
    

vector_fs = np.reshape(image_data_fs, [np.prod(np.array(image_data_fs.shape))])
vector_fw = np.reshape(image_data_fw, [np.prod(np.array(image_data_fw.shape))])
vector_msd = np.reshape(image_data_msd, [np.prod(np.array(image_data_fw.shape))])


brain_segment = 3035 and 4035


vector_fw[vector_fs != brain_segment] = 0
vector_msd[vector_fs != brain_segment] = 0
#vector_msd[vector_msd >= 15] = 0


print(pearsonr(vector_fw, vector_msd))


plt.plot(vector_fw, vector_msd, 'ro')

    
    


    

