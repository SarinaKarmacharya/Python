#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 09:18:05 2017

@author: sarina karmacharya
"""

from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from medpy.io import load
import numpy as np
import seaborn as sns
import pandas as pd

fw_array = []


caselist = open("caselist.csv",'r+')


for line in caselist:
    casenumber = line.rstrip()
    
    
    image_data_fw, image_header_fw = load('{0}_FW.nii' .format(casenumber))
    
    vector_fw = np.reshape(image_data_fw, [np.prod(np.array(image_data_fw.shape))])
    
    
    in_m = (vector_fw != 1.0)
    keep1 = np.where(in_m)
    last_vector_fw = vector_fw[keep1]
    
    average_fw = np.mean(last_vector_fw)
    fw_array.append(average_fw)


caselist.close()

age_array = []

agelist = open("age.csv",'r+')

for line in agelist:
    age =  line.rstrip()
    
    age_array.append(float(age))
    
agelist.close()

#############

fw_array = []


caselist = open("caselist_control.csv",'r+')


for line in caselist:
    casenumber = line.rstrip()
    
    
    image_data_fw, image_header_fw = load('{0}_FW.nii' .format(casenumber))
    
    vector_fw = np.reshape(image_data_fw, [np.prod(np.array(image_data_fw.shape))])
    
    
    in_m = (vector_fw != 1.0)
    keep1 = np.where(in_m)
    last_vector_fw = vector_fw[keep1]
    
    average_fw = np.mean(last_vector_fw)
    fw_array.append(average_fw)


caselist.close()

age_array = []

agelist = open("age_control.csv",'r+')

for line in agelist:
    age =  line.rstrip()
    
    age_array.append(float(age))
    
agelist.close()


data={'FW': fw_array,'AGE': age_array }
d = pd.DataFrame(data)

data1={'FW ': fw_array, 'AGE ': age_array}
d1 = pd.DataFrame(data1)


f, ax = plt.subplots()
ax.set(xlim=(7.8, 14.1), ylim=(0.25, 0.31))


sns.plt.title('FW and Age Correlation', size = 21)

    
z, x = (pearsonr(age_array, fw_array))

t, s = (pearsonr(age_array, fw_array))


sns.regplot(x="AGE", y="FW", robust=True, data=d, ci = None, scatter_kws = {'color':'red'}, line_kws = {'color':'red'})

sns.regplot(x="AGE ", y="FW ", robust=True, data=d1, ci = None, scatter_kws = {'color':'blue'}, line_kws = {'color':'blue'})
    

sns.plt.ylabel("Free Water", size = 16)
sns.plt.xlabel("Age", size = 16)


green_line = mpatches.Patch(color = 'red')
    
blue_line = mpatches.Patch(color = 'blue')

plt.legend([green_line, blue_line], ['Control = {0}' .format(z), 'A= {0}' .format(t)], prop = {'size': 12})

    

    
    
sns.plt.show()
