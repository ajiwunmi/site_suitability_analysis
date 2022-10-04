import folium
import streamlit as st
from folium.plugins import Draw
from streamlit_folium import st_folium

import pandas as pd
import geopandas
import streamlit as st

    df = pd.DataFrame(
        {'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
        'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
        'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
        'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})
    
    gdf = geopandas.GeoDataFrame(
        df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
   
    st.write(gdf.head())
   
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    ax = world[world.continent == 'South America'].plot(
        color='white', edgecolor='black')
    gdf.plot(ax=ax, color='red')
    st.pyplot()

# st.set_page_config(layout="wide")

## Try drawing some objects and then clicking on them"

# m = folium.Map(location=[39.949610, -75.150282], zoom_start=5)
# Draw(export=True).add_to(m)

# c1, c2 = st.columns(2)
# with c1: 
#     st.write('No show')   
#     # output = st_folium(m, width = 700, height=500)

# with c2:
#     st.write('show')