import json
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
#font = {"family":"IPAGothic"}
mpl.rc('font', **font)
#plt.tight_layout()


data = pd.read_json('counted_Roselia.json')
data = data.drop([1,3,4,6,13])
print(data.iloc[:25])
#plt.bar(data.iloc[0:20][0], data.iloc[0:20][1], color='magenta')
plt.bar(data.iloc[0:15][0], data.iloc[0:15][1], color='indigo')
plt.xticks(rotation=90)
plt.xlabel('word')
plt.ylabel('frequency')
plt.title("Roselia")
#plt.savefig("PoppinParty_count.png", dpi=300)
plt.show()

