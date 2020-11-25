
import fastbook
fastbook.setup_book()

from fastbook import *
from fastai.vision.widgets import *

def search_images(subscription_key , search_term):
    search_url = "https://api.bing.microsoft.com/v7.0/images/search"
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": search_term, "license": "public", "imageType": "photo", "count": "150"}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    return search_results


key = input("Bing API key: ")
