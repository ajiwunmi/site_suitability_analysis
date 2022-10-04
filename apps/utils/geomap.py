import pandas as pd
import requests


def load_location():

    base_url =  "https://nominatim.openstreetmap.org/search?format=json"
    postcode = "63101"
    response = requests.get(f"{base_url}&postalcode={postcode}&country=United States")
    data = response.json()

    # St Louis latitude and longitude
    latitude = data[0].get("lat")
    longitude = data[0].get("lon")

    # st.write(latitude + ' '+longitude ) 
    
    # map of St Louis
    location = float(latitude), float(longitude)
    
    return location