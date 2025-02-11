import requests
import pandas as pd
import time
import schedule

# API URL for fetching top 50 cryptocurrencies
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
    "sparkline": "false"
}

def fetch_crypto_data():
    """Fetches live cryptocurrency data from CoinGecko API."""
    try:
        response = requests.get(API_URL, params=PARAMS)
        data = response.json()
        
        # Extract required fields
        crypto_list = []
        for coin in data:
            crypto_list.append({
                "Name": coin["name"],
                "Symbol": coin["symbol"].upper(),
                "Price (USD)": coin["current_price"],
                "Market Cap": coin["market_cap"],
                "24h Volume": coin["total_volume"],
                "24h Change (%)": coin["price_change_percentage_24h"]
            })

        df = pd.DataFrame(crypto_list)
        return df
    
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    print(fetch_crypto_data().head())  # Test the function
