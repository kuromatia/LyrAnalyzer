mport json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

#---setiing---------------------------------
sns.set()
sns.set_style("whitegrid")
sns.set_context(context="paper", font_scale=2)
#sns.set_context({"lines.linewidth":3})
#mpl.rcParams['axes.xmargin'] = 0.5
#mpl.rcParams['axes.ymargin'] = 0.5
#rcParams.update({'figure.autolayout': True})
#--------------------------------------------
font = {"family":"TakaoPGothic"}
mpl.rc('font', **font)
#plt.tight_layout()


data = pd.read_json('counted_PoppinParty.json')
plt.bar(data.iloc[0:20][0], data.iloc[0:20][1], color='purple')
plt.xticks(rotation=90)
plt.xlabel('word')
plt.ylabel('freq')
plt.show()

