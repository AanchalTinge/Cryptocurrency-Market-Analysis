from fetch_crypto_data import fetch_crypto_data

def analyze_data(df):
    """Performs basic analysis on the cryptocurrency data."""
    if df.empty:
        print("No data available for analysis.")
        return None
    
    top_5 = df.nlargest(5, "Market Cap")[["Name", "Market Cap"]]
    avg_price = df["Price (USD)"].mean()
    highest_24h_change = df.nlargest(1, "24h Change (%)")[["Name", "24h Change (%)"]]
    lowest_24h_change = df.nsmallest(1, "24h Change (%)")[["Name", "24h Change (%)"]]

    analysis_result = {
        "Top 5 Cryptos by Market Cap": top_5.to_dict(orient="records"),
        "Average Price of Top 50 Cryptos": avg_price,
        "Highest 24h Change": highest_24h_change.to_dict(orient="records"),
        "Lowest 24h Change": lowest_24h_change.to_dict(orient="records")
    }

    return analysis_result

if __name__ == "__main__":
    df = fetch_crypto_data()
    analysis = analyze_data(df)
    print(analysis)
