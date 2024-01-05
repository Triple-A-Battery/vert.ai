import requests
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi import FastAPI
from supabase import create_client, Client

import ai_model
import price_pred
import stock_info

supabase: Client = create_client(
    "https://eobauqgsolxvyamddpjl.supabase.co",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVvYmF1cWdzb2x4dnlhbWRkcGpsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDQzNzc4OTcsImV4cCI6MjAxOTk1Mzg5N30.hJx5GMmCS6PWnRio9hOJB04ZkoO5Cf-WD_O1zjc7yRI",
)
app = FastAPI()


# Configure CORS to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    # Allow sending credentials (cookies, etc.) with requests
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
async def read_root():
    return None


@app.get("/check_stock")
async def generate(
    open: float, esg: float, pe: float, roe: float, days: int = 1, stock: str = None
):
    if stock:
        response = (
            supabase.table("STOCKS").select("*").eq("stock_name", stock).execute()
        )

    if not stock or not response[1][0]["investment_check"]:
        response = bool(
            ai_model.generate_data(
                pd.DataFrame(
                    [[days, open, esg, pe, roe]],
                    columns=[
                        "horizon (days)",
                        "price_BUY",
                        "ESG_ranking",
                        "PE_ratio",
                        "roe_ratio",
                    ],
                )
            )[0]
            == 1
        )
        if stock:
            supabase.table("STOCKS").update({"investment_check": response}).eq(
                "stock_name", stock
            ).execute()
    return response


@app.get("/future")
async def generate(open: float, high: float, low: float, volume: int, days: int = 7):
    return price_pred.generate(open, high, low, volume, days)


@app.get("/charities")
async def charities(page: str = "1"):
    url = "https://www.globalgiving.org/dy/v2/search/query"
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    }

    data = {
        "size": "60",
        "nextPage": page,
        "sortField": "sortorder",
        "keywords": "",
        "selectedLocations": "00india",
        "currencyInfo": "%5Bobject+Object%5D",
        "recognitionNames": "%5Bobject+Object%5D",
        "recognitionDescs": "%5Bobject+Object%5D",
    }

    response = requests.post(url, headers=headers, data=data)
    data = response.json()
    hits = data["hits"]["hits"]

    d = []
    for c in hits:
        d.append(
            {
                "name": c["_source"]["orgname"],
                "desc": c["_source"]["projsummary"],
                "themes": c["_source"]["allthemes"],
                "url": c["_source"]["url"],
                "progress": c["_source"]["percent_funded"],
            }
        )
    return d


@app.get("/fetch_info/{ticker}")
async def fetch_info(ticker: str):
    data = stock_info.fetch_data(ticker)
    return data


@app.get("/news")
async def news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "green finance",
        "from": "2023-12-05",
        "sortBy": "publishedAt",
        "apiKey": "f63ff11703ac44e4aef7305ca4a4f887",
    }

    response = requests.get(url, params=params).json()["articles"]
    return response
