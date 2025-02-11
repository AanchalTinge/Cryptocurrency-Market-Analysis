from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import matplotlib.pyplot as plt
import pandas as pd
import os
from analyze_crypto_data import analyze_data
from fetch_crypto_data import fetch_crypto_data
from update_excel import update_excel  # Import update_excel function

# Define file paths
PDF_FILE = "crypto_report.pdf"
IMAGE_FILE = "chart.png"

def generate_chart(df):
    """Generates a bar chart of the top 5 cryptocurrencies by market cap."""
    top_5 = df.nlargest(5, "Market Cap")
    plt.figure(figsize=(6, 4))
    plt.bar(top_5["Name"], top_5["Market Cap"], color=['blue', 'green', 'red', 'purple', 'orange'])
    plt.xlabel("Cryptocurrency")
    plt.ylabel("Market Cap (USD)")
    plt.title("Top 5 Cryptos by Market Cap")
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.savefig(IMAGE_FILE)
    plt.close()

def generate_pdf():
    """Creates a PDF report with cryptocurrency analysis."""
    df = fetch_crypto_data()
    analysis = analyze_data(df)
    generate_chart(df)
    update_excel()  # Ensure Excel is updated before generating the PDF
    
    c = canvas.Canvas(PDF_FILE, pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 50, "Live Cryptocurrency Report")
    
    # Summary
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Total Market Cap: ${df['Market Cap'].sum():,.2f}")
    c.drawString(50, height - 100, f"Average Price: ${df['Price (USD)'].mean():,.2f}")
    
    # Top 5 Cryptos by Market Cap
    y = height - 140
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Top 5 Cryptos by Market Cap:")
    c.setFont("Helvetica", 10)
    y -= 20
    for coin in analysis.get("Top 5 Cryptos by Market Cap", []):
        name = coin.get("Name", "N/A")
        symbol = coin.get("Symbol", "N/A")
        market_cap = coin.get("Market Cap", 0)
        c.drawString(60, y, f"{name} ({symbol}): ${market_cap:,}")
        y -= 15
    
    # Price Change Analysis
    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Price Change Analysis (24h %):")
    y -= 20
    c.setFont("Helvetica", 10)
    highest = analysis.get("Highest 24h Change", [{}])[0]
    lowest = analysis.get("Lowest 24h Change", [{}])[0]
    c.drawString(60, y, f"Highest: {highest.get('Name', 'N/A')} ({highest.get('24h Change (%)', 0):.2f}%)")
    y -= 15
    c.drawString(60, y, f"Lowest: {lowest.get('Name', 'N/A')} ({lowest.get('24h Change (%)', 0):.2f}%)")
    
    # Insert Chart Image
    if os.path.exists(IMAGE_FILE):
        c.drawImage(ImageReader(IMAGE_FILE), 50, y - 150, width=500, height=300)
    
    c.save()
    print(f"PDF Report '{PDF_FILE}' generated successfully.")

if __name__ == "__main__":
    generate_pdf()
