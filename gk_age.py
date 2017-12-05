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

gk_array_adhd = []


caselist = open("caselist.csv",'r+')


for line in caselist:
    casenumber = line.rstrip()
    
    
    image_data_gk, image_header_gk = load('{0}_GK.nii' .format(casenumber))
    
    vector_gk = np.reshape(image_data_gk, [np.prod(np.array(image_data_gk.shape))])

    
    average_gk = np.mean(vector_gk)
    gk_array_adhd.append(average_gk)


caselist.close()

age_array = []

agelist = open("age.csv",'r+')

for line in agelist:
    age =  line.rstrip()
    
    age_array.append(float(age))
    
agelist.close()


#########

gk_array = []


caselist = open("caselist_control.csv",'r+')


for line in caselist:
    casenumber = line.rstrip()
    
    
    image_data_gk, image_header_gk = load('{0}_GK.nii' .format(casenumber))
    
    vector_gk = np.reshape(image_data_gk, [np.prod(np.array(image_data_gk.shape))])

    
    average_gk = np.mean(vector_gk)
    gk_array.append(average_gk)


caselist.close()

age_array = []

agelist = open("age_control.csv",'r+')

for line in agelist:
    age =  line.rstrip()
    
    age_array.append(float(age))
    
agelist.close()


data={'GK': gk_array,'AGE': age_array }
d = pd.DataFrame(data)

data1={'GK': gk_array, 'AGE ': age_array}
d1 = pd.DataFrame(data1)


f, ax = plt.subplots()
ax.set(xlim=(7.8, 14.2), ylim=(3, 13))


sns.plt.title('GK and Age Correlation', size = 21)

    
z, x = (pearsonr(age_array, gk_array))

t, s = (pearsonr(age_array_adhd, gk_array_adhd))


sns.regplot(x="AGE", y="GK", robust=True, data=d, ci = None, scatter_kws = {'color':'red'}, line_kws = {'color':'red'})

sns.regplot(x="AGE", y="GK ", robust=True, data=d1, ci = None, scatter_kws = {'color':'blue'}, line_kws = {'color':'blue'})
    

sns.plt.ylabel("General Kurtosis", size = 16)
sns.plt.xlabel("Age", size = 16)


green_line = mpatches.Patch(color = 'red')
    
blue_line = mpatches.Patch(color = 'blue')

plt.legend([green_line, blue_line], ['Control = {0}' .format(z), 'A = {0}' .format(t)], prop = {'size': 12})

    

    
    
sns.plt.show()

