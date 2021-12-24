from io import StringIO
import os
import sys
import pandas as pd
from pycaret.regression import *
from pydantic import BaseModel
import cloudpickle

sys.path.append(os.getcwd())

class MainCore():

    def get_df_from_binary(self, binary):
        s = str(binary, 'utf-8')
        data = StringIO(s) 
        df = pd.read_csv(data, sep=';')
        return df

    def predict_response(self, input_json):
        df = pd.json_normalize(input_json.input)

        model = load_model('models/nxt_day_temp_prediction_et_22_12_2021_feat_sel')

        new_predictions = predict_model(model, data=df)

        return round(float(new_predictions['Label'].value), 1)

if __name__ == '__main__':


    class InputJson(BaseModel):
        input = {}

    input_json = InputJson()

    input_json.input={
        'station': 1.0,
        'Present_Tmax': 29.2,
        'Present_Tmin': 21.5,
        'LDAPS_RHmin': 59.24028015,
        'LDAPS_RHmax': 85.28312683,
        'LDAPS_Tmax_lapse': 29.91538275,
        'LDAPS_Tmin_lapse': 22.13205443,
        'LDAPS_WS': 7.295952598,
        'LDAPS_LH': 111.038305,
        'LDAPS_CC1': 0.306907301,
        'LDAPS_CC2': 0.08745181,
        'LDAPS_CC3': 0.480662905,
        'LDAPS_CC4': 0.271983078,
        'lat': 37.6046,
        'lon': 126.991,
        'DEM': 212.335,
        'Slope': 2.785,
        'Solar radiation': 5275.070313
    }

    predCore = MainCore()

    predCore.predict_response(input_json)