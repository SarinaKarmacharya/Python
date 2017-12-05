#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:38:56 2017

@author: sarina karmacharya
"""

from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
from medpy.io import load
import numpy as np


caselist = open("caselist.txt",'r+')


for line in caselist:
    casenumber = line.rstrip()


    image_data_msd, image_header_msd = load('{0}_MSD.nii' .format(casenumber))
    image_data_fw, image_header_fw = load('{0}_FW.nii' .format(casenumber))
    image_data_fs, image_header_fs = load("{0}_wmparc-in-bse.nii.gz" .format(casenumber))
    

    vector_fw = np.reshape(image_data_fw, [np.prod(np.array(image_data_fw.shape))])
    vector_msd = np.reshape(image_data_msd, [np.prod(np.array(image_data_msd.shape))])
    vector_fs = np.reshape(image_data_fs, [np.prod(np.array(image_data_fs.shape))])
    


    gray_matter = {1028,1027,1032,1020,1019,1018,1014,1003,1012,1024,1017,1002,1026,1011,1013,1005,1021,1008,1029,1031,1025,1022,1023,1010,1009,1015,1030,1033,1034,1007,1006,1016,2028,2027,2032,2020,2019,2018,2014,2003,2012,2024,2017,2002,2026,2011,2013,2005,2021,2008,2029,2031,2025,2022,2023,2020,2009,2015,2030,2033,2034,2007,2006,2016}
    
    id=[]
    for i in gray_matter:
        gray=(vector_fs==i)
        k=np.where(gray)
        shape=vector_fw[k]
        id.append(shape)
    
    gray_fw=np.concatenate((id[0:len(id)]))
    
    id1=[]
    for i in gray_matter:
        gray=(vector_fs==i)
        k1=np.where(gray)
        shape1=vector_msd[k1]
        id1.append(shape1)
        
    gray_msd=np.concatenate((id1[0:len(id1)]))
    
    in_l = (gray_msd <= 15)
    keep = np.where(in_l)
    final_gray_msd = gray_msd[keep]
    final_gray_fw = gray_fw[keep]
    
    in_k = (final_gray_msd != 0)
    keep1 = np.where(in_k)
    ultimate_gray_msd = final_gray_msd[keep1]
    ultimate_gray_fw = final_gray_fw[keep1]

    in_m = (ultimate_gray_fw != 1.0)
    keep2 = np.where(in_m)
    last_gray_msd = ultimate_gray_msd[keep2]
    last_gray_fw = ultimate_gray_fw[keep2]
    
    
    z = np.polyfit(last_gray_fw, last_gray_msd, 1)
    p = np.poly1d(z)
    plt.plot(last_gray_fw, p(last_gray_fw), 'b--')
    
    
    t, s = (pearsonr(last_gray_fw, last_gray_msd))


caselist.close()

plt.ylabel("Gray Matter Mean Square Displacement")
plt.xlabel("Gray Matter Free Water")
    
    
plt.savefig('correlation_trendlines.png' .format(casenumber), bbox_inches = 'tight')
    
    
plt.show()
