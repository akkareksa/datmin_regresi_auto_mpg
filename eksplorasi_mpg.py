# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:20:39 2019

@author: User
"""

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('auto_mpg.csv', index_col='car_name') 
# cara menfilter berdasarkan kolom horsepower dan menampilkan kolom tertentu
clean_frame = df.loc[df.horsepower>0]

# plot
clean_frame.plot(kind='scatter',x='horsepower',y='mpg')
plt.title('Scatter Horsepower-MPG')
plt.xlabel('horsepower')
plt.ylabel('mpg')
plt.show()