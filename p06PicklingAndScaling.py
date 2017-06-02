import math
import pandas as pd
import quandl
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')

api_key = "Cxe41MDVyJhXQYGuVGx7"

# df = quandl.get('WIKI/GOOGL', authtoken=api_key)

# df.to_pickle("linearRegressionDataframe.pickle")
df = pd.read_pickle("linearRegressionDataframe.pickle")

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low'])/ df['Adj. Low'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

df.dropna(inplace = True)

forecast_col = 'Adj. Close'
df.fillna(value = -99999,inplace = True)
forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)



X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace = True)
y = np.array(df['label'])


X_train, X_text , y_train , y_test = train_test_split(X,y,test_size=0.2)

# clf = LinearRegression(n_jobs=-1)
# clf.fit(X_train,y_train)
#
# with open('linearregression.pickle','wb') as f:
#     pickle.dump(clf,f)

pickle_in = open('linearregression.pickle','rb')
clf = pickle.load(pickle_in)


accuracy = clf.score(X_text,y_test)
print(accuracy)

forecast_set = clf.predict(X_lately)

# print(forecast_set,accuracy,forecast_out)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix = next_unix + one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()

plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# print(df.tail())
