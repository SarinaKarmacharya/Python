#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:44:37 2017

@author: vs796
"""

from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
from medpy.io import load
import numpy as np


caselist = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/caselist.txt",'r+')


for line in caselist:
    casenumber = line.rstrip()


    image_data_msd, image_header_msd = load('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/MSD/{0}_MSD.nii' .format(casenumber))
    image_data_fw, image_header_fw = load('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/FW/{0}_FW.nii' .format(casenumber))
    image_data_fs, image_header_fs = load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/freesurferINdwi/{0}_wmparc-in-bse.nii.gz" .format(casenumber))
    

    vector_fw = np.reshape(image_data_fw, [np.prod(np.array(image_data_fw.shape))])
    vector_msd = np.reshape(image_data_msd, [np.prod(np.array(image_data_msd.shape))])
    vector_fs = np.reshape(image_data_fs, [np.prod(np.array(image_data_fs.shape))])
    


    white_matter = {3028,3027,3032,3020,3019,3018,3014,3003,3012,3024,3017,3002,3026,3011,3013,3005,3021,3008,3029,3031,3025,3022,3023,3010,3009,3015,3030,3033,3034,3007,3006,3016,4028,4027,4032,4040,4019,4018,4014,4003,4012,4024,4017,4002,4026,4011,4013,4005,4021,4008,4029,4031,4025,4022,4023,4020,4009,4015,4030,4033,4034,4007,4006,4016}
    
    id=[]
    for i in white_matter:
        white=(vector_fs==i)
        k=np.where(white)
        shape=vector_fw[k]
        id.append(shape)
    
    white_fw=np.concatenate((id[0:len(id)]))
    
    id1=[]
    for i in white_matter:
        white=(vector_fs==i)
        k1=np.where(white)
        shape1=vector_msd[k1]
        id1.append(shape1)
        
    white_msd=np.concatenate((id1[0:len(id1)]))
    
    
    in_l = (white_msd <= 15)
    keep = np.where(in_l)
    final_white_msd = white_msd[keep]
    final_white_fw = white_fw[keep]
    
    in_k = (final_white_msd != 0)
    keep1 = np.where(in_k)
    ultimate_white_msd = final_white_msd[keep1]
    ultimate_white_fw = final_white_fw[keep1]

    in_m = (ultimate_white_fw != 1.0)
    keep2 = np.where(in_m)
    last_white_msd = ultimate_white_msd[keep2]
    last_white_fw = ultimate_white_fw[keep2]
    
    
    z = np.polyfit(last_white_fw, last_white_msd, 1)
    p = np.poly1d(z)
    plt.plot(last_white_fw, p(last_white_fw), 'b--')
    
    
    t, s = (pearsonr(last_white_fw, last_white_msd))


caselist.close()


plt.ylabel("White Matter Mean Square Displacement")
plt.xlabel("White Matter Free Water")

    
plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/White_Matter/correlation_graphs/correlation_trendlines.png' .format(casenumber), bbox_inches = 'tight')
    

plt.show()
    