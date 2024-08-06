import uvicorn
from fastapi import FastAPI
from ipynb.fs.full.FunctionforPrediction import predict_price
from DataAuth import DataAuth
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
pickle_in = open("HousePricePrediction.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'working good server connected'}

@app.post('/predict')
def predict_house_price(data: DataAuth):
    data = data.model_dump()
    # print(data)
    location = data['location']
    sqft = data['sqft']
    bath = data['bath']
    bhk = data['bhk']
    # print(location, sqft, bath, bhk)
    price = predict_price(location, sqft, bath, bhk)
    return {
        "location": location,
        "sqft": sqft,
        "bath": bath,
        "bhk": bhk,
        "price": price
    }
