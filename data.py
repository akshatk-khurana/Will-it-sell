"""
Fetch images of top selling products from the Etsy developer's API and store them alongside a calculated
probability of them being sold (based off reviews and other sale metrics) in data-mappings.json
"""

import requests
import pillow