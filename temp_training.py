#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:53:57 2017

@author: vs796
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from medpy.io import load


t_statistic = []
p_value = []



fw_array = []
fw_array1 = []
fw_all = []
subject = []

case = open("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/case_list_temp.csv",'r+')

for line in case:
    casenumber = line.rstrip()


    image_data_fw, image_header_fw = load('/rfanfs/pnl-zorro/projects/ADHD/FW1000/Fwnii/{0}_FW.nii.gz' .format(casenumber))
    image_data_fs, image_header_fs = load("/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/freesurferINdwi/{0}_wmparc-in-bse.nii.gz" .format(casenumber))
    

    vector_fw = np.reshape(image_data_fw, [np.prod(np.array(image_data_fw.shape))])
    vector_fs = np.reshape(image_data_fs, [np.prod(np.array(image_data_fs.shape))])
        
    sub_cortical = {50,51,58,54,49,52,60,53,11,12,18,26,10,13,28,17}
    
    id=[]
    for i in sub_cortical:
        gray=(vector_fs==i)
        k=np.where(gray)
        shape=vector_fw[k]
        id.append(shape)
    
    gray_fw=np.concatenate((id[0:len(id)]))
    
    in_m = (gray_fw != 1.0)
    keep1 = np.where(in_m)
    last_gray_fw = gray_fw[keep1]

    
    average_gray_fw = np.mean(last_gray_fw)
    average_gray_all = np.mean(last_gray_fw)
    fw_all.append(average_gray_all)
    if casenumber.startswith('case1'):
        fw_array.append(average_gray_fw)
        sub = ('ADHD')
        subject.append(sub)
    else:
        fw_array1.append(average_gray_fw)
        sub1 = ('Control')
        subject.append(sub1)

    

case.close()

#############


data={'Values': fw_all,'Group': subject }

d = pd.DataFrame(data)


t, s = (stats.ttest_ind(fw_array, fw_array1, equal_var = False))
print(stats.ttest_ind(fw_array, fw_array1, equal_var = False))

t_statistic.append(t)
p_value.append(s)

from math import sqrt
cohens_d = (np.mean(fw_array) - np.mean(fw_array1)) / (sqrt((np.std(fw_array) ** 2 + np.std(fw_array1) ** 2) / 2))
print(cohens_d)

sns.set(style="whitegrid", palette="Set2")
sns.boxplot(x="Group", y="Values", data=d, whis=np.inf)
sns.swarmplot(x="Group", y="Values", color="0.1", data=d, size = 4.5)
ax = sns.swarmplot(x="Group", y="Values", color="0.1", data=d, size = 4.5, label = 't-value = {} \np-value = {} \ncohens-d = {}' .format(t,s,cohens_d))
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:1], labels[:1], prop = {'size':10.5}, loc = 9)
sns.plt.title('Subcortical: FW', size=20)
plt.xlabel("Group", size = 16)
plt.ylabel("FW Values", size = 16)
plt.show()
#    plt.savefig('/rfanfs/pnl-zorro/home/vidushi/ADHD_MSD_FW/final_graphs/{0}_fw.pdf' .format(roi), bbox_inches = 'tight')




