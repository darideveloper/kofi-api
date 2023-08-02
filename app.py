import os
import json
from datetime import datetime
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv ()

app = Flask(__name__)
KOFI_TOKEN = os.getenv("KOFI_TOKEN")

@app.post("/")
def home():
    
    # Get post data 
    form_data = request.form.get ("data")
    form_data = json.loads (form_data)
    res_token = form_data["verification_token"]
    timestamp = form_data["timestamp"]
    res_type = form_data["type"]
    from_name = form_data["from_name"]
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
    date = datetime.fromtimestamp (timestamp)
    
 
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)