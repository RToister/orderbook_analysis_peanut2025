import os
import requests
import logging

API_URL = os.getenv("API_URL", "https://api.example.com/orderbook")

def fetch_orderbook():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()

        return {
            "bids": [[float(price), float(volume)] for price, volume in data.get("bids", [])],
            "asks": [[float(price), float(volume)] for price, volume in data.get("asks", [])]
        }
    except requests.RequestException as e:
        logging.error(f"API request failed: {e}")
        return {"bids": [], "asks": []}
