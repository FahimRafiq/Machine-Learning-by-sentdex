import math
import pandas as pd
import quandl
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

api_key = "Cxe41MDVyJhXQYGuVGx7"

df = quandl.get('WIKI/GOOGL', authtoken=api_key)



df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low'])/ df['Adj. Low'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

df.dropna(inplace = True)

forecast_col = 'Adj. Close'
df.fillna(value = -99999,inplace = True)
forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace = True)

X = np.array(df.drop('label',1))
y = np.array(df['label'])

X = preprocessing.scale(X)

X_train, X_text , y_train , y_test = train_test_split(X,y,test_size=0.2)

clf = LinearRegression()
clf.fit(X_train,y_train)
accuracy = clf.score(X_text,y_test)
print(accuracy)
