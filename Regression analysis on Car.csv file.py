import pandas as pd
import numpy as np
import joblib
import sklearn

df=pd.read_csv("Car.csv")

df=df.dropna()
df=df.drop(columns='index')
df=df.reset_index(drop=True)

#print(df.isna().sum())

Cor=df.corr()

x=df.drop(columns=['selling_price','torque'])
y=df['selling_price']

def fn(a):
     a=a.split()
     return a[0]

x['mileage']=x['mileage'].apply(fn)
x['mileage']=x['mileage'].astype('float64')
#x['engine']=x['engine'].astype('float64') --> Conversion Error, same for 
                                             # max_power column

x['max_power']=x['max_power'].apply(fn)

ind=0
for i in range(len(x)):
    try:
        float(x.iloc[i,-2])
    except:
        ind=i
        
x=x.drop(index=ind)
y=y.drop(index=ind)
x=x.reset_index(drop=True)
y=y.reset_index(drop=True)
x['max_power']=x['max_power'].astype('float64')

x['engine']=x['engine'].apply(fn)

ind=0
for i in range(len(x)):
    try:
        float(x.iloc[i,-3])
    except:
        ind=i
        
x=x.drop(index=ind)
y=y.drop(index=ind)
x=x.reset_index(drop=True)
y=y.reset_index(drop=True)
x['engine']=x['engine'].astype('float64')


x['owner']=x['owner'].replace({'Fifth':'Fourth & Above Owner'})

x['name']=x['name'].apply(fn)

a=x['name'].value_counts()
for i in range(len(a)):
    if a[i]<15:
        x=x.replace({a.index[i]:'Others'})
        

from sklearn.preprocessing import LabelEncoder
lo=LabelEncoder()
x['owner']=lo.fit_transform(x['owner'])
le=LabelEncoder()
x['transmission']=le.fit_transform(x['transmission'])


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer([('encoder',OneHotEncoder(sparse=False),[0,3,4])],remainder='passthrough')
x=ct.fit_transform(x)


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(x)


from sklearn.model_selection import train_test_split as tts
x_train,x_test,y_train,y_test=tts(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression as LR
regressor=LR()
regressor.fit(x_train,y_train)
y_pred=regressor.predict(x_test)

from sklearn.metrics import r2_score
print(r2_score(y_test,y_pred))

joblib.dump(lo,'owner.joblib')
joblib.dump(le,'transmission.joblib')
joblib.dump(ct,'onehot.joblib')
joblib.dump(sc,'scaler.joblib')
joblib.dump(regressor,'regressor.joblib')
