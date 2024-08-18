# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

path1 =r'D:\Mathematical_Modeling\training\rate.csv'

# 豪看
color1 = "#106391"
color2 = "#fbe5c3"

rgb_color1 = mcolors.hex2color(color1)
rgb_color2 = mcolors.hex2color(color2)

custom_cmap = mcolors.LinearSegmentedColormap.from_list('custom', [rgb_color1, rgb_color2], N=256)

df = pd.read_csv(path1)


plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'

plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False 

plt.figure(figsize=(12,10))
sns.heatmap(df.corr(), annot=True, cmap=custom_cmap)
plt.xticks(rotation=18)
plt.title('相关系数热力图')
plt.show()
