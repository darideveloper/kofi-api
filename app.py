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

def write_data (seheets_manager:SheetsManager, sheet:str, data:list):
    """ Write data in specific sheet

    Args:
        sheet (str): sheet name
        data (list): data to write
    """
    
    # Change sheet
    seheets_manager.set_sheet (sheet)

    # Detect last row
    current_row = seheets_manager.get_rows_num () + 1

    # Write data
    seheets_manager.write_data ([data], row=current_row, column=1)

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
    
    # Format shop items
    if shop_items:
        shop_items_text = ""
        for shop_item in shop_items:
            shop_items_text += f"{shop_item['direct_link_code']} x{shop_item['quantity']}"
            variant = shop_item["variation_name"]
            if variant:
                shop_items_text += f" ({variant})"
            shop_items_text += f"\n"
        
    # Format shipping data
    if shipping:
        shipping_text = ""
        for shipping_key, shipping_value in shipping.items():
            shipping_text += f"{shipping_key}: {shipping_value}\n"
    
    # Connect to google sheets
    current_folder = os.path.dirname(os.path.abspath(__file__))
    creads_path = os.path.join (current_folder, "credentials.json")
    sheets = SheetsManager (GOOGLE_SHEETS, creads_path)
   
    # Write data based in donation type
    if res_type == "Donation":
        write_data (sheets, "kofi donations", [
            date, 
            time, 
            user_name, 
            message, 
            amount, 
            email, 
            currency
        ])        
    elif res_type == "Shop Order":
        write_data (sheets, "kofi sales", [
            date, 
            time, 
            user_name, 
            amount, 
            email, 
            currency, 
            shop_items_text, 
            shipping_text
        ])
         
    return ("ok")

if __name__ == "__main__":
    app.run(debug=True)