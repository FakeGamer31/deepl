import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import keras
import tensorflow as tf

data_df = pd.read_csv('Klassifikationsaufgabe.csv')

print(data_df.info())
print(data_df.describe())

data_df.sample(5)

sns.heatmap(data_df.isnull(), cbar=False).set_title('Fehlende Einträge')
plt.show()

boxplot = data_df.boxplot()
plt.show()

del data_df['Unnamed: 0']

boxplot = data_df.boxplot()
plt.show()

sns.distplot(data_df['Feature A'], color='g', bins=100, hist_kws={'alpha': 0.4})
plt.show()

corr = data_df.drop('Class', axis=1).corr()
sns.heatmap(corr[(corr >= 0.4) | (corr <= -0.4)],
            cmap='viridis', vmax=1.0, vmin=-1.0, linewidths=0.1,
            annot=True, annot_kws={"size": 8}, square=True);
plt.show()

for a in data_df:
    data_df[a] = data_df[a].fillna(data_df[a].median())

sns.heatmap(data_df.isnull(), cbar=False).set_title("Fehlende Einträge")
plt.show()

print(data_df.head())

X = data_df.drop('Class', axis=1)
y = data_df['Class']

scaler = MinMaxScaler()
X_trans = scaler.fit_transform(X)

selector = SelectKBest(score_func=chi2, k=2)
selector.fit_transform(X_trans, y)

cols_idx = selector.get_support(indices=True)
features_df = data_df.iloc[:, cols_idx]

print(features_df.head(5))
# X_train, X_test, y_train, y_test = train_test_split(features_df, y, test_size=0.33, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X_trans, y, test_size=0.33, random_state=42)
# Muss ich hier auch X benutzen oder kann ich das features_df benutzen?

model = keras.models.Sequential([
    keras.layers.Dense(5, activation = keras.activations.relu),
    keras.layers.Dense(10, activation = keras.activations.relu),
    keras.layers.Dense(3, activation = keras.activations.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

keras.utils.set_random_seed(354)
model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))

# model.evaluate(X_test, y_test)

# param_grid = {
#     'C': [0.1, 0.5, 1,1.5 ,2 ,2.5 ,3.5, 4, 4.5, 5, 10],
#     'gamma': [0.1, 0.5, 0.005, 0.3, 1, 1.5, 2, 2.5, 3, 3.5 ,4 ,5, 10],
#     'kernel': ['linear', 'rbf', 'sigmoid']
# }
#
# clf = GridSearchCV(estimator=svm.SVC(), param_grid=param_grid)
#
# clf.fit(X_train, y_train)
# print(clf.best_params_)
#
# svm_classificator = clf.best_estimator_
# print(svm_classificator)
#
# y_pred = svm_classificator.predict(X_test)
# print(accuracy_score(y_test, y_pred))
# print(classification_report(y_test, y_pred))
