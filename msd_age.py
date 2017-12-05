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
import scipy.stats as stats

msd_array_adhd = []
msd_array = []


caselist = open("/caselist.txt",'r+')


for line in caselist:
    casenumber = line.rstrip()
    
    
    image_data_msd, image_header_msd = load('{0}_MSD.nii' .format(casenumber))
    
    vector_msd = np.reshape(image_data_msd, [np.prod(np.array(image_data_msd.shape))])
    
    
    in_l = (vector_msd <= 15)
    keep = np.where(in_l)
    final_vector_msd = vector_msd[keep]
    
    in_k = (final_vector_msd != 0)
    keep1 = np.where(in_k)
    ultimate_vector_msd = final_vector_msd[keep1]
    
    average_msd = np.mean(ultimate_vector_msd)
    if casenumber.startswith('case1'):
        msd_array_adhd.append(average_msd)
    else:
        msd_array.append(average_msd)


caselist.close()

age_array_adhd = []

agelist_adhd = open("age_adhd.csv",'r+')

for line in agelist_adhd:
    age =  line.rstrip()
    
    age_array_adhd.append(float(age))
    
agelist_adhd.close()


#########


age_array = []

agelist = open("age_control.csv",'r+')

for line in agelist:
    age =  line.rstrip()
    
    age_array.append(float(age))
    
agelist.close()


data={'MSD': msd_array,'AGE': age_array }
d = pd.DataFrame(data)

data1={'MSD': msd_array_adhd, 'AGE ': age_array_adhd}
d1 = pd.DataFrame(data1)


f, ax = plt.subplots()
ax.set(xlim=(7.8, 14.1), ylim=(2.3, 3.9))


sns.plt.title('MSD and Age Correlation', size = 21)

    
z, x = (pearsonr(age_array, msd_array))

t, s = (pearsonr(age_array_adhd, msd_array_adhd))


sns.regplot(x="AGE", y="MSD", robust=True, data=d, ci = None, scatter_kws = {'color':'red'}, line_kws = {'color':'red'})

sns.regplot(x="AGE", y="MSD", robust=True, data=d1, ci = None, scatter_kws = {'color':'blue'}, line_kws = {'color':'blue'})
    

sns.plt.ylabel("Mean Squared Displacement", size = 16)
sns.plt.xlabel("Age", size = 16)


green_line = mpatches.Patch(color = 'red')
    
blue_line = mpatches.Patch(color = 'blue')

plt.legend([green_line, blue_line], ['Control = {0}' .format(z), 'A = {0}' .format(t)], prop = {'size': 12})



plt.savefig('correlation_age_msd.png', bbox_inches = 'tight')
    
    
sns.plt.show()

