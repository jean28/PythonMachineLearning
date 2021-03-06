import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import StratifiedKFold

df = pd.read_csv('../data/wdbc.csv')

# Convert M (malign) and B (benign) into numbers

X = df.iloc[:, 2:].values
y = df.iloc[:, 1].values

le = LabelEncoder()
y = le.fit_transform(y)

le.transform(['M', 'B'])

# Divide Dataset into separate training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

pipe_lr = Pipeline([('scl', StandardScaler()),
                    ('pca', PCA(n_components=2)),
                    ('clf', LogisticRegression(random_state=1))])

pipe_lr.fit(X_train, y_train)

kfold = StratifiedKFold(n_splits=10, random_state=1)
kfold.get_n_splits(X_train, y_train)


scores = []

fold = 1
for train, test in kfold.split(X_train, y_train):
    pipe_lr.fit(X_train[train], y_train[train])
    score = pipe_lr.score(X_train[test], y_train[test])
    scores.append(score)
    print('Fold: %s, Class dist.: %s, Acc: %.3f' % (fold, np.bincount(y_train[train]), score))
    fold += 1

print('CV accuracy: %.3f +/- %.3f' % (np.mean(scores), np.std(scores)))