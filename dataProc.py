
import pandas as pd
import seaborn as sb
import numpy as np

df=pd.read_csv("src/datasets/ESS10.csv")

question_mapping = {
"netusoft": "How often do you use the internet? (1-5, high - often)",
"ppltrst": "trust in people (0-10, high - trust)",
"pplfair": "people take advantage of you or try to be fair? (0-10, high - fair)",
"pplhlp": "Would you say that most of the time people try to be helpful or that they are mostly looking out for themselves? (0-10, high - helpful)",
"trstprl": "On a scale of 0-10 how much do you personally trust each of the following institutions? [Country]’s parliament? (0-10, high-trust)",
"trstlgl": "On a scale of 0-10 how much do you personally trust each of the following institutions? The legal system? (0-10, high-trust)",
"trstplc": "On a scale of 0-10 how much do you personally trust each of the following institutions? The police? (0-10, high-trust)",
"trstplt": "On a scale of 0-10 how much do you personally trust each of the following institutions? The politicians? (0-10, high-trust)",
"trstprt": "On a scale of 0-10 how much do you personally trust each of the following institutions? The political parties? (0-10, high-trust)",
"stflife": "All things considered, how satisfied are you with your life as a whole nowadays? (0-10, high-satisfied)",
"stfeco": "On the whole how satisfied are you with the present state of the economy in [Country]?  (0-10, high-satisfied)",
"stfgov":  "Now thinking about the [Country] government, how satisfied are you with the way it is doing its job?  (0-10, high-satisfied)",
"stfdem":  "On the whole, how satisfied are you with the way democracy works in [Country]?  (0-10, high-satisfied)",
"stfedu": "What do you think overall about the state of education in [Country] nowadays? (0-10, high-satisfied)",
"stfhlth":"What do you think overall about the state of health services in [Country] nowadays?  (0-10, high-satisfied)",
"happy": "Taking all things together, how happy would you say you are? (0-10, high-happy)",
"sclmeet": "How often do you meet socially with friends, relatives or work colleagues? (1-7, high-often)",
"inprdsc": "How many people, if any, are there with whom you can discuss intimate and personal matters? (0-6, high-more)",
"fairelcc":"Please indicate to what extent you think each of the following statements applies in [Country]. National elections in [Country] are free and fair. (0-10, high-fair/free)",
"hscopc19": "How satisfied are you with the way health services in [Country] coped with the coronavirus pandemic and its consequences? (0-10, high-satisfied)",
"vdovexre":"How would you rate the overall experience of taking part in this survey? (0-10, high-positive experience)",
"inprdsc": "How many people, if any, are there with whom you can discuss intimate and personal matters with? (0-6, 0 = None, 1 =1, 2 = 2, 3 = 3, 4 = 4-6, 5 = 7-9, 6 = 10 or more)",
"gvimpc19_": "To what extent do you trust the national government in [Country] to deal with the impact of the coronavirus pandemic? (0-10, high-satisfied)",
"gvhanc19": "Overall, how satisfied are you with the [Country] government’s handling of the coronavirus pandemic? (0-10, Extremely satisfied)",
"keydecc": "Please indicate to what extent you think this statement applies in [Country]. Key decisions in [Country] are made by the national government rather than the European Union. (0-10, high - applies completely)",

"cttresac":  "Please indicate to what extent you think this statement applies in [Country]. The courts in [Country] treat everyone the same. (0-10, high- applies completely)",

"medcrgvc": "Please indicate to what extent you think this statement applies in [Country]. The media in [Country] are free to criticise the government. (0-10, high - applies completely)",

"imwbcnt": "Is [country] made a worse or a better place to live by people coming to live here from other countries?  (0-10, hihg - better place to live)",

"imueclt": "Would you say that [country]'s cultural life is generally undermined or enriched by people coming to live here from other countries? (0-10, high - cultural life enriched)",

"imbgeco": "Would you say it is generally bad or good for [country]'s economy that people come to live here from other countries?  (0-10, high - good for the economy)",
"aesfdrk": "How safe do you, or would you, feel walking alone in the area you live in after dark? (1-4, high-unsafe)",
"health": "How is your health in general? (1-5)",
"hincfel": "Which of the descriptions on this card comes closest to how you feel about your household's income nowadays? (1-4) "
}

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
#TODO
result = result.drop(
    ['edlvpdfi', 'edlvpeno', 'fampref', 'edlvfebg', 'famadvs', 'fampdf', 'edlvmdahu', 'edlvmebg', 'edlvdpt'], axis=0)

print(result)

negCorr = result[result.iloc[:, 0] < -0.2]
posCorr= result[result.iloc[:, 0] > 0.2]

allCorr= negCorr.append(posCorr);


sb.heatmap(posCorr, annot=True, fmt="g", cmap='RdBu_r')
#sb.heatmap(result2, annot=True, fmt="g", cmap='RdBu_r')

#plt.show()

negCorr.columns = ['values']
posCorr.columns = ['values']
allCorr.columns = ['values']
negCorr.index.name = "labels"
posCorr.index.name = "labels"
allCorr.index.name = "question"

allCorr['values'] = allCorr['values'].abs()

allCorr['identifier'] = allCorr.index
allCorr= allCorr.transpose().rename(columns=question_mapping).transpose()
allCorr= allCorr.sort_values(by="values", ascending=False )

descriptions = np.array(["Happiness",
    "General life satisfaction",
               "Feeling about household income",
               "Satisfaction with country's economy",
               "Satisfaction with country's education",
               "Satisfaction with country's health services",
               "Satisfaction with country's democracy",
               "Trust in country's police",
               "Perception of fairness in people's behavior",
               "Personal health in general",
               "Trust in country's parliament",
               "Trust in people",
               "Satisfaction with how country's health services coped with coronavirus pandemic",
               "Trust in country's legal system",
               "Perceived fairness in national election",
               "Perception of helpfulness in people's behavior",
               "Satisfaction with national government",
               "Personal safety while walking alone at night",
               "Personal comfort in discussing intimate topics in personal relationships",
               "Internet usage frequency",
               "Trust in how the government dealt with the impact of coronavirus pandemic",
               "Perception of how free the media is to criticize the government",
               "Perception of whether immigration positively impacts country’s cultural life",
               "Overall rating of survey experience",
               "Trust in country’s politicians",
               "Perception of whether immigration positively impacts country's living conditions",
               "Satisfaction with country's government handling of pandemic",
               "Frequency of social meetings with friends, relatives and colleagues",
               "Perception of equal treatment in court",
               "Perception importance for democracy that national governments handle key issues rather than EU",
               "Trust in country’s political parties",
               "Perception of whether immigration positively affects country's economy"])


allCorr['labels'] = descriptions.tolist()

#csv_ng= negCorr.to_csv("ESS10-happy-negCorr-bigger-02.csv");
#csv_pos= posCorr.to_csv("ESS10-happy-posCorr-bigger-02.csv");
csv_all= allCorr.to_csv("src/datasets/ESS10-happy-allCorr-bigger-02.csv");

# csv_values_ng= negCorr.to_csv("ESS10-happy-negCorr-bigger-0.2_values",  columns=['values'], index=False, header=False );
# csv_labels_ng= negCorr.to_csv("ESS10-happy-negCorr-bigger-0.2_labels", columns=[], header=False);
#
# csv_values_pos= posCorr.to_csv("ESS10-happy-posCorr-bigger-0.2_values", columns= ['values'], index=False ,header=False);
# csv_labels_pos= posCorr.to_csv("ESS10-happy-posCorr-bigger-0.2_labels", columns=[], header=False);

# csv_values_ng_str = ','.join(str(element) for element in csv_values_ng)
# with open("ESS10-happy-negCorr-bigger-0.2_values.txt", "w") as text_file:
#     text_file.write(csv_values_ng_str)


# csv_file = r'ESS10-happy-negCorr-bigger-0.2_values.csv'
# txt_file = r'ESS10-happy-negCorr-bigger-0.2_values.txt'
# with open(txt_file, "w") as my_output_file:
#     with open(csv_file, "r") as my_input_file:
#         reader = csv.reader(my_input_file)
#         my_output_file.write(','.join(row[0] for row in reader))

# create label file


label_file = pd.DataFrame()
label_file['identifier'] = allCorr['identifier']
label_file['values'] = allCorr['values']



