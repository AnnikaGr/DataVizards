
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

df=pd.read_csv("ESS10.csv")

# clean data
df = df.drop(df[df.ppltrst >= 11].index)
df = df.drop(df[df.pplfair >= 11].index)
df = df.drop(df[df.pplhlp >= 11].index)
df = df.drop(df[df.trstprl >= 11].index)
df = df.drop(df[df.trstlgl >= 11].index)
df = df.drop(df[df.trstplc >= 11].index)
df = df.drop(df[df.trstplt >= 11].index)
df = df.drop(df[df.trstprt >= 11].index)
df = df.drop(df[df.stflife >= 11].index)
df = df.drop(df[df.stfeco >= 11].index)
df = df.drop(df[df.stfgov >= 11].index)
df = df.drop(df[df.stfdem >= 11].index)
df = df.drop(df[df.stfedu >= 11].index)

df = df.drop(df[df.stfhlth >= 11].index)
df = df.drop(df[df.happy >= 11].index)
df = df.drop(df[df.sclmeet >= 11].index)
df = df.drop(df[df.inprdsc >= 11].index)
df = df.drop(df[df.fairelcc >= 11].index)
df = df.drop(df[df.fairelcc >= 11].index)

df = df.drop(df[df.hscopc19 >= 11].index)

df = df.drop(df[df.aesfdrk >= 7].index)
df = df.drop(df[df.health >= 7].index)
df = df.drop(df[df.netusoft >= 7].index)
df = df.drop(df[df.hincfel >= 7].index)

df = df.drop(df[df.inprdsc  >= 6].index)

df = df.drop(df[df.gvimpc19 >= 11].index)
df = df.drop(df[df.gvhanc19 >= 11].index)
df = df.drop(df[df.keydecc >= 11].index)
df = df.drop(df[df.cttresac  >= 11].index)
df = df.drop(df[df.medcrgvc  >= 11].index)
df = df.drop(df[df.imwbcnt  >= 11].index)
df = df.drop(df[df.imueclt  >= 11].index)
df = df.drop(df[df.imbgeco  >= 11].index)

print("Df row count: " + str(len(df)));

# calculate correlations
pearsoncorr= df.corrwith(df['happy'], method ="spearman")
result= pearsoncorr.to_frame()
print(result)

negCorr = result[result.iloc[:, 0] < -0.2]
posCorr= result[result.iloc[:, 0] > 0.2]

sb.heatmap(posCorr, annot=True, fmt="g", cmap='RdBu_r')
#sb.heatmap(result2, annot=True, fmt="g", cmap='RdBu_r')

plt.show()

negCorr.to_csv("ESS10-happy-negCorr-bigger-0.2");
posCorr.to_csv("ESS10-happy-posCorr-bigger-0.2");

