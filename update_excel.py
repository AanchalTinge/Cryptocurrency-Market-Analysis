import pandas as pd
import schedule
import time
from fetch_crypto_data import fetch_crypto_data
from analyze_crypto_data import analyze_data

# Define the Excel file name
EXCEL_FILE = "live_crypto_data.xlsx"

def format_analysis_for_excel(analysis):
    """Formats the analysis data into a structured DataFrame for writing to Excel."""
    formatted_data = []
    
    if "Top 5 Cryptos by Market Cap" in analysis:
        formatted_data.append(["Metric", "Cryptocurrency", "Value"])  # Add header row
        for coin in analysis["Top 5 Cryptos by Market Cap"]:
            formatted_data.append(["Top 5 Market Cap", coin["Name"], f"${coin['Market Cap']:,}"])
    
    if "Average Price of Top 50 Cryptos" in analysis:
        formatted_data.append(["Average Price", "", f"${analysis['Average Price of Top 50 Cryptos']:.2f}"])
    
    if "Highest 24h Change" in analysis:
        highest = analysis["Highest 24h Change"][0]
        formatted_data.append(["Highest 24h Change", highest["Name"], f"{highest['24h Change (%)']:.2f}%"])
    
    if "Lowest 24h Change" in analysis:
        lowest = analysis["Lowest 24h Change"][0]
        formatted_data.append(["Lowest 24h Change", lowest["Name"], f"{lowest['24h Change (%)']:.2f}%"])
    
    return pd.DataFrame(formatted_data)

def update_excel():
    """Fetches data, performs analysis, and updates the Excel file."""
    df = fetch_crypto_data()
    
    if df.empty:
        print("No data fetched. Skipping update.")
        return
    
    analysis = analyze_data(df)
    
    with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl", mode="w") as writer:
        df.to_excel(writer, sheet_name="Live Data", index=False)
        
        if analysis:
            analysis_df = format_analysis_for_excel(analysis)
            analysis_df.to_excel(writer, sheet_name="Analysis", index=False, header=False)

    print(f"Excel file updated successfully at {time.strftime('%Y-%m-%d %H:%M:%S')}")

# Schedule updates every 5 minutes
schedule.every(5).minutes.do(update_excel)

if __name__ == "__main__":
    print("Starting live updates for Excel sheet...")
    update_excel()  # Run once before scheduling
    while True:
        schedule.run_pending()
        time.sleep(60)
