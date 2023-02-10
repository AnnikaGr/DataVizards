
import pandas as pd
import numpy as np
import seaborn as sb

df=pd.read_csv("ESS10.csv")
print("The dataframe is:")
print(df)

interesting_factors= ["netuse", # - Personal use of internet/e-mail/www
                      "pplfair", # - Most people try to take advantage of you, or try to be fair
"pplhlp", #  - Most of the time people helpful or mostly looking out for themselves
"pplhlp", # - Most of the time people helpful or mostly looking out for themselves
"cptppol", # - Confident in own ability to participate in politics
"dmcntov", # - How democratic [country] is overall
"polintr", # - How interested in politics
"stfgov" , # - How satisfied with the national government
"stfhlth", # - State of health services in country nowadays
"stflife", # - How satisfied with life as a whole
"trstlgl", # - Trust in the legal system
"trstplt", # - Trust in politicians
"trstprt", # - Trust in political parties
"imdfetn", # - Allow many/few immigrants of different race/ethnic group from majority
"volunfp", # - Volunteered for not-for-profit or charitable organisation
"hhmmb", # - Number of people living regularly as member of household
"age", # - Age of respondent, calculated
"ablrtr", # - Worried not being able to retire at the age you would like to
"atncrse", # - Improve knowledge/skills: course/lecture/conference, last 12 months
"dvrcdev" , #- Ever been divorced (0/1)
"hincfel", # - Feeling about household's income nowadays
"estsz" , # - Establishment size
"hinctnt", # - Household's total net income, all sources(J → N)
"orgwrk", # - To what extent organise own work
"rmhhus", # - Number of rooms household have use of (not kitchens/bathrooms/toilets)
"wkhtot" , #- Total hours normally worked per week in main job overtime included
]

pearsoncorr = df.corr(method='pearson')
sb.heatmap(pearsoncorr,
           xticklabels=pearsoncorr.columns,
           yticklabels=pearsoncorr.columns,
           cmap='RdBu_r',
           annot=True,
           linewidth=0.5)