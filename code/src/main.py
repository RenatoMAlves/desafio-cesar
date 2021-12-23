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
from pycaret.regression import *
from pycaret.utils import check_metric

sys.path.append(os.getcwd())

class MainCore():

    def __init__(self):
        mlflow.set_tracking_uri("http://0.0.0.0:5000")

    def get_df_from_binary(self, binary):
        s = str(binary, 'utf-8')
        data = StringIO(s) 
        df = pd.read_csv(data, sep=';')
        return df

    def predict_response(self, contents):
        # df = pd.read_csv('~/Documents/CESAR/Desafio/dataset/Bias_correction_ucl_validation.csv', sep=',')
        df = self.get_df_from_binary(contents)

        model = load_model('code/models/nxt_day_temp_prediction_et_22_12_2021_baseline')

        new_predictions = predict_model(model, data=df)

        new_predictions = new_predictions.rename({'Label': 'Next_Tmax'}, axis=1)

        return new_predictions

if __name__ == '__main__': # pragma: no cover
    predCore = MainCore()

    predCore.predict_response('')