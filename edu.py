import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('/Users/msyzdykova/Downloads/kaggle-survey-2021/kaggle_survey_2021_responses.csv')
df=df.iloc[1:, :]
df.head()
#World population stats
#age
age=pd.DataFrame(df['Q1'].value_counts())
age=age.reset_index(drop=False)
age.columns=['Age', 'Count']
plt.figure()
plt.pie(age['Count'], autopct='%1.1f%%') #make % labels smaller ?
plt.legend(age['Age'], loc='upper center', bbox_to_anchor=(-1,1))
plt.title('Age')
#gender
gen=pd.DataFrame(df['Q2'].value_counts())
gen=gen.reset_index(drop=False)
gen.columns=['Gen', 'Count']
plt.figure()
plt.pie(gen['Count'], autopct='%1.1f%%') #make % labels smaller ?
plt.legend(gen['Gen'], loc='upper center', bbox_to_anchor=(-1,1))
plt.title('Gender')
#education
edu=pd.DataFrame(df['Q4'].value_counts())
edu=edu.reset_index(drop=False)
edu.columns=['Education', 'Count']
plt.figure()
plt.pie(x=edu['Count'])
plt.legend(edu['Education'], loc='upper center', bbox_to_anchor=(-1,1))
plt.title('Education')
#education breakdown by continents
continents=pd.read_csv('/Users/msyzdykova/Downloads/2020 Continents.csv')
continents_dict={k:v for k,v in zip(continents['Country'], continents['Continents'])}
df['Continents']=df['Q3'].map(continents_dict)
asia=df[df['Continents']=='Asia']
america=df[df['Continents']=='America']
europe=df[df['Continents']=='Europe']
africa=df[df['Continents']=='Africa']
australia=df[df['Continents']=='Australia']
others=df[df['Continents']=='Others']
#asia
asia_count=pd.DataFrame(asia['Q4'].value_counts())
asia_count=asia_count.reset_index(drop=False)
asia_count.columns=['Education', 'Count']
plt.figure()
plt.pie(x=asia_count['Count'])
plt.legend(asia_count['Education'], loc='upper center', bbox_to_anchor=(-1,1))
plt.title('Asia')
#europe
europe_count=pd.DataFrame(europe['Q4'].value_counts())
europe_count.head()
europe_count=europe_count.reset_index(drop=False)
europe_count.columns=['Education', 'Count']
plt.figure()
plt.pie(x=europe_count['Count'])
plt.legend(europe_count['Education'], loc='upper center', bbox_to_anchor=(-1,1))
plt.title('Europe')
#France
france=europe[europe['Q3']=='France']
france_count=pd.DataFrame(france['Q4'].value_counts())
france_count=france_count.reset_index(drop=False)
france_count.columns=['Education', 'Count']
plt.figure()
plt.figure(figsize=(20,9))
plt.bar(france_count['Education'], france_count['Count'])
plt.title('France')
#current job
job=pd.DataFrame(df['Q5'].value_counts())
job=job.reset_index(drop=False)
job.columns=['Job','Count']
plt.figure()
sns.barplot(data=job, y='Job', x='Count')
#language
Q7={}
for i in range(1,13):
    Q7.update(dict(df[f'Q7_Part_{i}'].value_counts()))
Q7=pd.DataFrame(Q7.items(), columns=['Language', 'Count'])
Q7
plt.figure()
plt.pie(Q7['Count'])
plt.legend(Q7['Language'], loc='upper center', bbox_to_anchor=(-1,1))
#ide
Q9={}
for i in range(1,13):
    Q9.update(dict(df[f'Q9_Part_{i}'].value_counts()))
Q9=pd.DataFrame(Q9.items(), columns=['IDE', 'Count'])
Q9
plt.figure()
plt.pie(Q9['Count'])
plt.legend(Q9['IDE'], loc='upper center', bbox_to_anchor=(-1,1))
#data visualization
Q14={}
for i in range(1, 12):
    Q14.update(dict(df[f'Q14_Part_{i}'].value_counts()))
Q14=pd.DataFrame(Q14.items(), columns=['Vis', 'Count'])
Q14
plt.figure()
sns.barplot(data=Q14, x='Count', y='Vis', orient='h')
#NLP
#compare Russia & India
rus=df[df['Q3']=='Russia']
ind=df[df['Q3']=='India']
Q19_r={}
for i in range(1, 6):
    Q19_r.update(dict(rus[f'Q19_Part_{i}'].value_counts()))
Q19_r=pd.DataFrame(Q19_r.items(), columns=['NLP', 'Count'])
plt.figure()
sns.barplot(data=Q19_r, x='Count', y='NLP').set(title='Russia')
Q19_i={}
for i in range(1, 6):
    Q19_i.update(dict(ind[f'Q19_Part_{i}'].value_counts()))
Q19_i=pd.DataFrame(Q19_i.items(), columns=['NLP', 'Count'])
plt.figure()
sns.barplot(data=Q19_i, x='Count', y='NLP').set(title='India')









    