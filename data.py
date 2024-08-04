"""
Fetch images of top selling products from the Etsy developer's API and store them alongside a calculated
probability of them being sold (based off reviews and other sale metrics) in data-mappings.json
"""

import requests
import JSON
from PIL import *

URL = ""
API_KEY = ""

req = requests.get(URL)
print(req.status_code)

image_urls = None

for image in image_urls:
    with open('image_name.jpg', 'wb') as f:
        f.write()