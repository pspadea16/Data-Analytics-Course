import pandas as pd
df=pd.Data({
    'name':
 ['matt','lisa','richard','john','Julia','jane','marlon'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'state':['DC','CO','DE','VA','MD','DE','NY'],
    'years of service':[10,0,2,0,2,1,5],
    'iq':[300,100,110,200,300,10,40]
})
rows=df.sample(frac=.25)
if(0.25*(len(df))==len(rows)):
    print(len(df),len(rows))
print'sample of 25%', 'rows'
groupby_gender=df.groupsby('gender')
for gender, value in groupby_gender['iq']:
    print((gender,value.mean())))
SumofAge=df['age'].sum()
print'Sum of Ages',SumofAge
MeanAge=df['age'].mean()
print'Average Ages', MeanAge
print('Means of each column',df.mean(axis=0))
print df['iq'].describe()

