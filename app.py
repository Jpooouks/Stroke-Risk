import pickle
from fastapi import FastAPI
import numpy as np
import pandas as pd
from pydantic import BaseModel

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

class InputData(BaseModel):
    data: dict

@app.post("/predict")
async def predict(input_data: InputData):
    X = pd.DataFrame(input_data.data)
    prediction = model.predict(X)
    return {"prediction": int(prediction[0])}