'''Seaborn is a plotting library built on top of matplotlib and can make plots look fancier'''

import seaborn as sns 
import matplotlib as plt
sns.set_theme(style='whitegrid')
tips = sns.load_dataset("tips")
ax = sns.boxplot(x="day", y="total_bill", data=tips)