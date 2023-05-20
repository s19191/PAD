import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import statsmodels.formula.api as smf

df = pd.read_csv('PAD_09_PD.csv', delimiter=";")
df.rename(columns={'Spending Score (1-100)':'Spending_Score','Annual Income (k$)':'Annual_Income'}, inplace=True,)
df['Gender'] = df['Gender'].apply(lambda x: x.replace('Male', '0'))
df['Gender'] = df['Gender'].apply(lambda x: x.replace('Female', '1'))

model = smf.ols(formula='Spending_Score ~ Gender + Age + Annual_Income', data=df).fit()

plt.clf()
sns.set()
corr_matrix = df.corr()
print(corr_matrix)
heatMapDf = pd.DataFrame(corr_matrix)
ax = sns.heatmap(corr_matrix)
plt.show()

print(model.summary())

print('P values: ', model.pvalues.values)
print('Coefficients: ', model.params.values)
print('Standard dev: ', model.bse.values)

px.scatter(df,'Annual_Income','Spending_Score','Gender',title='Spending score with Gender and Annual income').show()

px.scatter(df,'Annual_Income','Spending_Score','Age',title='Spending score with Age and Annual income').show()

px.scatter(df,'Age','Spending_Score','Gender',title='Spending score with Age and Gender').show()

px.scatter(df,'Age','Annual_Income','Gender',title='Annual income with Age and Gender').show()

pval = model.pvalues.values
print('P value max: ', pval.max())
print('P value max: ', pval.min())
modelNoGender = smf.ols(formula='Spending_Score ~ Age + Annual_Income', data=df).fit()
print(modelNoGender.summary())

px.scatter(df,'Annual_Income','Spending_Score',title='Spending score with Annual income').show()

px.scatter(df,'Annual_Income','Spending_Score','Age',title='Spending score with Age and Annual income').show()

px.scatter(df,'Age','Spending_Score',title='Spending score with Age').show()

px.scatter(df,'Age','Annual_Income',title='Annual income with Age').show()

modelNoAnnualIncome = smf.ols(formula='Spending_Score ~ Age + Gender', data=df).fit()
print(modelNoAnnualIncome.summary())

px.scatter(df,'Gender','Spending_Score',title='Spending score with Annual income').show()

px.scatter(df,'Gender','Spending_Score','Age',title='Spending score with Age and Annual income').show()

px.scatter(df,'Age','Spending_Score',title='Spending score with Age').show()

px.scatter(df,'Age','Gender',title='Annual income with Age').show()