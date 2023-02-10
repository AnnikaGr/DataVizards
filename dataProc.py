
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

df=pd.read_csv("ESS10.csv")

pearsoncorr= df.corrwith(df['happy'], method ="spearman")
result= pearsoncorr.to_frame()
print(result)

result1 = result[result.iloc[:, 0] < -0.2]
result2= result[result.iloc[:, 0]> 0.2]

sb.heatmap(result1, annot=True, fmt="g", cmap='RdBu_r')
#sb.heatmap(result2, annot=True, fmt="g", cmap='RdBu_r')

plt.show()

