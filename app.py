from fastapi import FastAPI, Path, HTTPException, Query
import json
from fastapi.responses import JSONResponse
import pandas as pd
from schema.user_input import UserInput
from Model.predict import predict_sentiment

print("Loading app.py...")

app = FastAPI()

@app.get("/home")
def home():
    return {'message': 'This is an API to predict sentiment using LSTMs for a movie review'}

@app.get("/health")
def health():
    return {'status': 'OK','version': '1.0'}


@app.post("/predict")
def predict(user_input: UserInput):
    try:
        from fastapi.responses import JSONResponse

        input_text = user_input.text
        output = predict_sentiment(input_text)
        return output
    except Exception as e:
        return JSONResponse(status_code=400, content = str(e))