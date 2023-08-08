import os
import json
from datetime import datetime as dt
from flask import Flask, request
from dotenv import load_dotenv
from spreadsheets.google_sheets import SheetsManager
from email_manager.sender import EmailManager
from kofi_query import query

load_dotenv ()

app = Flask(__name__)
KOFI_TOKEN = os.getenv("KOFI_TOKEN")
GOOGLE_SHEETS = os.getenv("GOOGLE_SHEETS")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_SUBJECT_STORE = os.getenv("EMAIL_SUBJECT_STORE")
DEBUG_EMAIL_TO = os.getenv("DEBUG_EMAIL_TO")

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
EMAIL_MANAGER = EmailManager (EMAIL_USER, EMAIL_PASS)

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
    
    try:
                
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
        url = form_data["url"]
        
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
        sheets_manager = SheetsManager (GOOGLE_SHEETS, creads_path)
    
        # Write data based in donation type
        subject = ""
        if res_type == "Donation":
            subject = f"Thanks for your support to {EMAIL_SUBJECT_STORE}!"
            write_data (sheets_manager, "kofi donations", [
                date, 
                time, 
                user_name, 
                message, 
                amount, 
                email, 
                currency,
                url,
            ]) 
        elif res_type == "Shop Order":

            # Create list of product links

            # Format shop items
            shop_items_text = []
            shop_items_links = []
            for shop_item in shop_items:
                
                # Create links of products
                product_link = f"https://ko-fi.com/s/{shop_item['direct_link_code']}"
                shop_items_links.append (product_link)
                
                # Query product name
                query_data = query (product_link, res_type)
                product_name = query_data["product_name"]
                                
                shop_item_text = f"{product_name} x{shop_item['quantity']}"
                variant = shop_item["variation_name"]
                if variant:
                    shop_item_text += f" ({variant})"
                shop_items_text.append (shop_item_text)

            # Format shipping data
            shipping_text = ""
            for shipping_key, shipping_value in shipping.items():
                shipping_text += f"{shipping_key}: {shipping_value}\n"
            
            subject = f"Thanks for purchasing {EMAIL_SUBJECT_STORE}!"
            write_data (sheets_manager, "kofi sales", [
                date, 
                time, 
                user_name, 
                amount, 
                email, 
                currency, 
                "\n".join(shop_items_text),
                "\n".join(shop_items_links),
                shipping_text,
                url,
            ])
        elif res_type == "Commission":


            query_data = query (url, res_type)
            product_name = query_data["product_name"]
            adiitional_details = query_data["adiitional_details"]
            
            subject = f"Thanks for your comission {EMAIL_SUBJECT_STORE}!"
            write_data (sheets_manager, "kofi comissions", [
                date, 
                time, 
                user_name, 
                amount, 
                email, 
                currency, 
                product_name,
                adiitional_details,
                url,
            ])
            
        # Get other donations data
        EMAIL_MANAGER.send_email (
            receivers=["darideveloper@gmail.com"],
            subject="test donations",
            body=str(form_data)
        )
            
        # Submit thaks email
        if subject == "":
            return ("no valid type", 400)
        
        print (f"Sending confirmation email to {email}...")
        EMAIL_MANAGER.send_email (
            receivers=[email],
            subject=subject,
            html_path=os.path.join(CURRENT_FOLDER, "templates", "thanks.html"),
            html_data={"user_name": user_name, "res_type": res_type}    
        )
        print ("Email sent")
            
        return ("ok")
    
    except Exception as e:
        
        print (e)
        
        # Submit error email
        EMAIL_MANAGER.send_email (
            receivers=[DEBUG_EMAIL_TO],
            subject="Error in Kofi Webhook",
            body=str(e) 
        )
        print ("Debug email sent")
        
        return ("error", 500)

if __name__ == "__main__":
    app.run(debug=True)