import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib

from sklearn.linear_model import LogisticRegression

model_url_path = 'heart.csv'
df = pd.read_csv(model_url_path)


def describe(dc):
    desc = dc.describe()
    return desc


print(df.columns)
drop_cols = ['sex', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
df = df.drop(drop_cols,  axis=1)
print(df)


def null_check(dc):
    nc = dc.isna().sum() / len(dc)
    return nc


def correlate(dc):
    corr = dc.corr()
    return corr


print('==' * 35)
print(correlate(df))
print('==' * 35)
print(null_check(df))
print('==' * 35)
X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80)
svc = SVC()
svc.fit(X, y)
print(svc.predict(X))
print(svc.score(X, y))
joblib.dump(svc, 'model.pkl')
