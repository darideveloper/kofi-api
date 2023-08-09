import requests
from bs4 import BeautifulSoup

def query (url:str, query_type:str) -> dict: 
    """ Manual query data from kofi pages

    Args:
        url (str): url to query
        query_type (str): name of the query type: Donation, Commission or Shop Order

    Returns:
        dict: data of the query:
            Commission: {product_name, adiitional_details, country}
            Shop Order: {product_name}
    """

    type = "Commission"

    page_data = {}
    selectos = {
        "commission": {
            "product_name": ".modal-dialog.modal-lg .row span:nth-child(3).kfds-font-size-16",
            "adiitional_details": ".modal-dialog.modal-lg .row .kfds-font-size-16.line-breaks.break-long-words",
            "country": '#supporterAddress',
            "full_address": '#supporterAddress',
        },
        "shop order": {
            "product_name": ".shop-item-title",
        }    
    }

    # Request with user agent
    current_selectors = selectos[type.lower()]

    if current_selectors:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'})
        soup = BeautifulSoup(res.text, "html.parser")

        for selector_name, selector_value in current_selectors.items():
            try:
                text = soup.select(selector_value)[0].text.strip().replace("\r", "")
            except:
                text = "not found"
                
            # Extra clean and format
            if selector_name == "country":
                text = text.split (",")[-1].strip()
            
            page_data[selector_name] = text


    return page_data