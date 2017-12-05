#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 09:10:00 2017

@author: vs796
"""

import matplotlib.pyplot as plt
from medpy.io import load
import numpy as np
import seaborn as sns


caselist = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/caselist.txt",'r+')


for line in caselist:
    casenumber = line.rstrip()


    image_data_msd, image_header_msd = load('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/MSD/{0}_MSD.nii' .format(casenumber))
    image_data_fw, image_header_fw = load('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/FW/{0}_FW.nii' .format(casenumber))
    image_data_fs, image_header_fs = load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/freesurferINdwi/{0}_wmparc-in-bse.nii.gz" .format(casenumber))
    

    vector_fw = np.reshape(image_data_fw, [np.prod(np.array(image_data_fw.shape))])
    vector_msd = np.reshape(image_data_msd, [np.prod(np.array(image_data_msd.shape))])
    vector_fs = np.reshape(image_data_fs, [np.prod(np.array(image_data_fs.shape))])
    


    sub_cortical = {50,51,58,54,49,52,60,53,11,12,18,26,10,13,28,17}
    
    id=[]
    for i in sub_cortical:
        subcortical=(vector_fs==i)
        k=np.where(subcortical)
        shape=vector_fw[k]
        id.append(shape)
    
    subcortical_fw=np.concatenate((id[0:len(id)]))

    id1=[]
    for i in sub_cortical:
        subcortical=(vector_fs==i)
        k1=np.where(subcortical)
        shape1=vector_msd[k1]
        id1.append(shape1)

    subcortical_msd=np.concatenate((id1[0:len(id1)]))

    in_l = (subcortical_msd <= 15)
    keep = np.where(in_l)
    final_subcortical_msd = subcortical_msd[keep]
    final_subcortical_fw = subcortical_fw[keep]

    in_k = (final_subcortical_msd != 0)
    keep1 = np.where(in_k)
    ultimate_subcortical_msd = final_subcortical_msd[keep1]
    ultimate_subcortical_fw = final_subcortical_fw[keep1]

    in_m = (ultimate_subcortical_fw != 1.0)
    keep2 = np.where(in_m)
    last_subcortical_msd = ultimate_subcortical_msd[keep2]
    last_subcortical_fw = ultimate_subcortical_fw[keep2]
    
    sns.plt.ylabel("Subcortical Mean Square Displacement")
    sns.plt.xlabel("Subcortical Free Water") 


    f, ax = plt.subplots()
    ax.set(xlim=(0, 1.0), ylim=(0, 7))
    ax = sns.regplot(last_subcortical_fw, last_subcortical_msd, robust = True, ci = None, scatter = False, line_kws = {'color':'blue'})



caselist.close()

    
#plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/Subcortical/correlation_graphs/correlation_trendlines.png', bbox_inches = 'tight')
    
plt.show()
