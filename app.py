import os
import json
from datetime import datetime as dt
from flask import Flask, request
from dotenv import load_dotenv
from spreadsheets.google_sheets import SheetsManager
from email_manager.sender import EmailManager

load_dotenv ()

app = Flask(__name__)
KOFI_TOKEN = os.getenv("KOFI_TOKEN")
GOOGLE_SHEETS = os.getenv("GOOGLE_SHEETS")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
DEBUG_EMAIL_TO = os.getenv("DEBUG_EMAIL_TO")

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

def write_data (sheets_manager:SheetsManager, sheet:str, data:list):
    """ Write data in specific sheet

    Args:
        sheet (str): sheet name
        data (list): data to write
    """
    
    # Change sheet
    sheets_manager.set_sheet (sheet)

    # Detect last row
    current_row = sheets_manager.get_rows_num () + 1

    # Write data
    sheets_manager.write_data ([data], row=current_row, column=1)

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
    sheets_manager = SheetsManager (GOOGLE_SHEETS, creads_path)
   
    # Write data based in donation type
    subject = ""
    if res_type == "Donation":
        subject = "Thanks for your support to nyxtrackers!"
        write_data (sheets_manager, "kofi donations", [
            date, 
            time, 
            user_name, 
            message, 
            amount, 
            email, 
            currency
        ])        
    elif res_type == "Shop Order":
        subject = "Thanks for purchasing nyxtrackers!"
        write_data (sheets_manager, "kofi sales", [
            date, 
            time, 
            user_name, 
            amount, 
            email, 
            currency, 
            shop_items_text, 
            shipping_text
        ])
        
    # Submit thaks email
    print (f"Sending confirmation email to {email}...")
    email_manager = EmailManager (EMAIL_USER, EMAIL_PASS)
    email_manager.send_email (
        receivers=[email],
        subject=subject,
        html_path=os.path.join(CURRENT_FOLDER, "templates", "thanks.html"),
        html_data={"user_name": user_name, "res_type": res_type}    
    )
    print ("Email sent!")
         
    return ("ok")

if __name__ == "__main__":
    app.run(debug=True)