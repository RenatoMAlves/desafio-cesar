from io import StringIO
import os
import sys
import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from mlflow import log_metrics, log_params, log_artifacts, set_tags
from mlflow.tracking import MlflowClient
from sklearn.pipeline import Pipeline

class MainCore():

    def __init__(self):
        mlflow.set_tracking_uri("http://0.0.0.0:5000")

    def get_df_from_binary(self, binary):
        s = str(binary, 'utf-8')
        data = StringIO(s) 
        df = pd.read_csv(data, sep=';')
        return df

    def predict_response(self, contents, date_ref_col, mlflow_id, target_name):
        df = self.get_df_from_binary(contents)

        X, y = df[df[~target_name]], df[target_name]
        X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=11)

        pipe = Pipeline([('scaler', StandardScaler()), ('lr', LinearRegression())])

        pipe.fit(X_train, y_train)
        pipe.score(X_test, y_test)

        return False

if __name__ == '__main__': # pragma: no cover
    predCore = MainCore()