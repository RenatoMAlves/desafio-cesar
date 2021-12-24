from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from pydantic import BaseModel
from src.main import MainCore
import cloudpickle

class InputJson(BaseModel):
    input = {}

app = FastAPI(
    title='desafio-cesar',
    description='Time Series Prediction',
    version='0.0.1')

pred = MainCore()

@app.get('/health')
def health():
  return {'status': 'OK'}

@app.get('/', include_in_schema=False)
def root():
    return RedirectResponse('/docs')

@app.post('/predict')
def predict(input_json: InputJson):

    prediction = pred.predict_response(input_json)

    return {'Prediction result:', prediction}
