📊 Live Cryptocurrency Market Analysis
🚀 This project fetches live cryptocurrency data, performs market analysis, and generates automated reports in Excel, Google Sheets, and PDF format.

📌 Features
✅ Fetches real-time crypto market data (price, market cap, volume, etc.)
✅ Performs data analysis (top performers, highest gainers/losers, market cap trends)
✅ Saves data to Excel & Google Sheets for remote access
✅ Generates a formatted PDF report with graphs & insights
✅ Automates updates for real-time tracking

📂 Project Structure
bash
Copy
Edit
📦 crypto-market-analysis  
 ┣ 📜 fetch_crypto_data.py        # Fetches live crypto data  
 ┣ 📜 analyze_crypto_data.py      # Performs analysis on fetched data  
 ┣ 📜 update_excel.py             # Saves data to an Excel file  
 ┣ 📜 update_google_sheets.py     # Pushes data to Google Sheets  
 ┣ 📜 generate_pdf.py             # Creates a formatted PDF report  
 ┣ 📜 requirements.txt            # Python dependencies  
 ┣ 📜 README.md                   # Project documentation  
 ┗ 📂 output/                     # Stores generated reports  
   ┣ 📜 crypto_data.xlsx  
   ┗ 📜 crypto_report.pdf  
⚙️ Installation & Setup
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/your-username/crypto-market-analysis.git
cd crypto-market-analysis
2️⃣ Install Dependencies
Ensure you have Python 3 installed, then run:

sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Scripts
Fetch and Analyze Data
sh
Copy
Edit
python fetch_crypto_data.py
python analyze_crypto_data.py
Save to Excel & Google Sheets
sh
Copy
Edit
python update_excel.py
python update_google_sheets.py
Generate PDF Report
sh
Copy
Edit
python generate_pdf.py
📊 Output Reports
📜 Excel File: crypto_data.xlsx
📄 PDF Report: crypto_report.pdf

The Excel and Google Sheets files allow real-time tracking, while the PDF report provides a formatted summary with graphs.

🔧 Configuration
🔹 Google Sheets API: Set up a Google API key and credentials to push live data to Google Sheets.
🔹 Task Automation: Use Task Scheduler (Windows) or Cron Jobs (Linux/Mac) to automate periodic updates.

🔗 API Used
This project uses a public cryptocurrency API to fetch real-time market data. Replace the API key in fetch_crypto_data.py if needed.

🚀 Future Enhancements
🔹 Add historical data analysis
🔹 Implement interactive dashboards (Dash/Streamlit)
🔹 Improve visualizations with advanced charts
🔹 Support for multiple API sources

