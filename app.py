import os
import json
from datetime import datetime as dt
from flask import Flask, request
from dotenv import load_dotenv
from spreadsheets.google_sheets import SheetsManager

load_dotenv ()

app = Flask(__name__)
KOFI_TOKEN = os.getenv("KOFI_TOKEN")
GOOGLE_SHEETS = os.getenv("GOOGLE_SHEETS")

@app.post("/")
def home():
    
    # Get post data 
    form_data = request.form.get ("data")
    form_data = json.loads (form_data)
    res_token = form_data["verification_token"]
    timestamp = form_data["timestamp"]
    res_type = form_data["type"]
    user_name = form_data["from_name"]
    message = form_data["message"]
    amount = form_data["amount"]
    email = form_data["email"]
    currency = form_data["currency"]
    shop_items = form_data["shop_items"]
    shipping = form_data["shipping"]
    
    # Validate token
    if res_token != KOFI_TOKEN:
        return ("Invalid token", 403)
    
    # Convert string to datetime
    datetime = dt.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
    date = datetime.strftime("%d/%m/%Y")
    time = datetime.strftime("%H:%M:%S")
    
    # Connect to google sheets
    current_folder = os.path.dirname(os.path.abspath(__file__))
    creads_path = os.path.join (current_folder, "credentials.json")
    sheets = SheetsManager (GOOGLE_SHEETS, creads_path, sheet_name="kofi")
   
    # Detect last row
    current_row = sheets.get_rows_num () + 1 
   
    # Detect donation type
    if res_type == "Donation":
        # Write data in google sheets
        sheets.write_data ([
            [date, time, user_name, message, amount, email, currency]
        ], row=current_row, column=1)
 
 
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)