from typing import Union
from pprint import pprint
import numpy as np
import pandas as pd
from fastapi import FastAPI

from ai_model import generate_data

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import keras
from keras.regularizers import l1_l2

import os
from supabase import create_client, Client

supabase: Client = create_client(
    "https://eobauqgsolxvyamddpjl.supabase.co",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVvYmF1cWdzb2x4dnlhbWRkcGpsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDQzNzc4OTcsImV4cCI6MjAxOTk1Mzg5N30.hJx5GMmCS6PWnRio9hOJB04ZkoO5Cf-WD_O1zjc7yRI",
)
app = FastAPI()


@app.get("/")
async def read_root():
    return None


@app.get("/check_supabase")
async def check_supabase():
    return "data"


@app.get("/generate")
async def generate():
    response, count = supabase.table("STOCKS").select("investment_check").execute()
    if response[1][0]["investment_check"] is None:
        data = pd.read_csv("./training_data.csv")
        response = generate_data(data)
    return response
