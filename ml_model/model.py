import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.linear_model import LogisticRegression

model_url_path = 'heart.csv'
df = pd.read_csv(model_url_path)


def describe(dc):
    desc = dc.describe()
    return desc


print(df.columns)
drop_cols = ['sex', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
df = df.drop(drop_cols, axis=1)
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
lr = LogisticRegression(max_iter=1000)
svc = SVC()

lr.fit(X, y)
svc.fit(X, y)

print(svc.predict(X))


svc_p = int(svc.score(X, y) * 100)
lr_p = int(lr.score(X, y) * 100)

dic = {
    'svm prediction': svc_p,
    'logistic regression prediction': lr_p
}

prediction_df = pd.DataFrame(dic, index=[0])
print(prediction_df)

sns.set();
fig = plt.figure()
langs = ['Logistic regression', 'Support vector machines']
students = [svc_p, lr_p]
bar_list = plt.bar(langs, students, width=0.3)
bar_list[0].set_color('crimson')
bar_list[1].set_color('green')
plt.ylabel("prediction score")
plt.show()


# print(svc.score(X, y))
print(
    'Logistic regression accuracy score is {0} while svm accuracy score is {1}'.format(lr.score(X, y) * 100, svc.score(X, y) * 100))
joblib.dump(lr, 'model.pkl')
