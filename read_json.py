import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from matplotlib import rcParams

#---setiing---------------------------------
sns.set()
sns.set_style("whitegrid")
sns.set_context(context="paper", font_scale=2)
#sns.set_context({"lines.linewidth":3})
#mpl.rcParams['axes.xmargin'] = 0.5
#mpl.rcParams['axes.ymargin'] = 0.5
rcParams.update({'figure.autolayout': True})
#--------------------------------------------
font = {"family":"TakaoPGothic"}
#font = {"family":"IPAGothic"}
mpl.rc('font', **font)
#plt.tight_layout()

artist = 'Afterglow'
name = 'counted_' + artist
data = pd.read_json(name + '.json')
data = data.drop([1,5,10,20,21,23])
print(data.iloc[:25])
#plt.bar(data.iloc[0:20][0], data.iloc[0:20][1], color='magenta')
plt.bar(data.iloc[0:15][0], data.iloc[0:15][1], color='red')
plt.xticks(rotation=90)
plt.xlabel('word')
plt.ylabel('frequency')
plt.tight_layout()
plt.title(artist)
plt.savefig(name +".png", dpi=300)
plt.show()

