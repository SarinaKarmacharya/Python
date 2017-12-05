# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:50:01 2017

@author: vs796
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from medpy.io import load
import numpy as np


sns.set(context = "paper", font = "monospace")


image_data_fs, image_header_fs = load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/freesurferINdwi/case104_wmparc-in-bse.nii.gz")
image_data_msd, image_header_msd = load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/MSD/case104_MSD.nii")
image_data_fw, image_header_fw = load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/FW/case104_FW.nii")

#vector_fs = np.reshape(image_data_fs, [np.prod(np.array(image_data_fs.shape))])
#vector_fw = np.reshape(image_data_fw, [np.prod(np.array(image_data_fw.shape))])
#vector_msd = np.reshape(image_data_msd, [np.prod(np.array(image_data_msd.shape))])


two_image_fw = np.array(np.reshape(image_data_fw,[110, 110*74]))
two_image_fs = np.array(np.reshape(image_data_fs,[110, 110*74]))
two_image_msd = np.array(np.reshape(image_data_msd,[110, 110*74]))


index = (two_image_fs == 3035)

in_o=np.equal(two_image_fs, 3035)
np.where()
[i for i, x in enumerate(in_o) if x]

df=index.DataFrame


final_matrix = np.delete(two_image_fw, index)
 
#image_data_fw[image_data_fs == 3035] = 0
#two_image_fw = np.reshape(image_data_fw,[image_data_fw.shape[0], np.prod(image_data_fw.shape[1],image_data_fw.shape[2])])
#two_image_fw = np.reshape(image_data_fw,[110, 110*74])
d = pd.DataFrame(data = final_matrix)
corrmat = d.corr()


f, ax = plt.subplots(figsize = (12, 9))


sns.heatmap(corrmat, square = True)


networks = corrmat.columns.get_level_values("network")
for i, network in enumerate(networks):
    if i and network != networks[i - 1]:
        ax.axhline(len(networks) - i, c = "w")
        ax.axvline(i, c = "w")
f.tight_layout()

