from fastapi.responses import RedirectResponse
from fastapi import FastAPI, BackgroundTasks, UploadFile, File
from starlette.requests import Request
from starlette.responses import Response
from pydantic import BaseModel
from src.main import MainCore

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

@app.post('/upload-and-predict')
async def upload_data_and_predict(dataset: UploadFile=File(...)):
    contents = await dataset.read()
    predict_stats = pred.predict_response(contents)

    return {"Message": "The data was preprocessed and predicted!"}
