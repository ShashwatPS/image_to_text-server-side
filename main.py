import os
import shutil

import uvicorn
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from sentiment_analysis.sentiment_v1 import predict_sentiment
from gemini_image.model import generate_description
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    url: str

@app.post("/upload/")
async def upload_file(item: Item):
    resp = generate_description(item.url)
    sentiment_prediction = predict_sentiment(resp)
    return {
        "url": item.url,
        "description": resp,
        "sentiment": sentiment_prediction
    }
