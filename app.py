import os
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv ()

app = Flask(__name__)
TOKEN = os.getenv("TOKEN")

@app.post("/")
def home():
    
    # Get post data 
    form_data = request.form
    
    
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)