#Here we train the model that that will be used in the deployment.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline
from sklearn import linear_model
from sklearn.metrics import roc_auc_score

import pickle

df = pd.read_csv('https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv')

df.columns = df.columns.str.lower().str.replace(' ', '_')

categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

for c in categorical_columns:
    df[c] = df[c].str.lower().str.replace(' ', '_')

df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')
df.totalcharges = df.totalcharges.fillna(0)

df.churn = (df.churn == 'Yes').astype(int)


df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

train_dict = df_full_train.drop(['churn'], axis=1).to_dict(orient='records')

test_dict = df_test.drop(['churn'], axis=1).to_dict(orient='records')

# Create a pipeline that includes a DictVectorizer and a Logistic Regression model.
# The DictVectorizer will convert the dictionary representation of the data into a format suitable for the model,
# and the Logistic Regression model will be used to predict churn.
pipeline = make_pipeline(
    DictVectorizer(sparse=False),
    linear_model.LogisticRegression(solver='liblinear', C=1.0, max_iter=1000, random_state=42)
)

pipeline.fit(train_dict, df_full_train.churn)

# Compute the AUC score on the test set
y_test_pred = pipeline.predict_proba(test_dict)[:, 1]

auc = roc_auc_score(df_test.churn, y_test_pred)
print(f'Test AUC score: {auc:.3f}')