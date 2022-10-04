import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import geopandas
import streamlit as st
import matplotlib.pyplot as plt
import shapefile
from os.path import isfile, exists
import os


def app():
    st.subheader('')
    absolute_path_to_file = os.path.abspath(os.curdir)+'/data/countries/countries.shp'

    # st.write(absolute_path_to_file)

    dbf = absolute_path_to_file.replace('.shp', '.dbf')
    # st.write(isfile(absolute_path_to_file))
    # st.write(exists(dbf))
    if isfile(absolute_path_to_file) and exists(dbf):
        shp = shapefile.Reader(absolute_path_to_file)
        # st.write(shp)
        # shp

    # st.title("Vector Map")

    # m = leafmap.Map(center=[0, 0], zoom=2)

    # in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable_geo.geojson'
    # m.add_geojson(in_geojson, layer_name="Cable lines")
    # filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    # m = leafmap.Map(tiles="stamentoner")
    # m.add_heatmap(
    #     filepath,
    #     latitude="latitude",
    #     longitude="longitude",
    #     value="pop_max",
    #     name="Heat map",
    #     radius=20,
    # )
    # m.to_streamlit(height=700)
   

    # df = pd.DataFrame(
    #     {'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
    #     'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
    #     'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
    #     'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})
    
    # gdf = geopandas.GeoDataFrame(
    #     df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
   
    # st.write(gdf.head())
   
    # world = geopandas.read_file(geopandas.datasets.get_path('nybb'))
    # fig, ax = plt.subplots()
    # st.write(world.BoroName)
    # ax = world[world.BoroName == 'St Louis'].plot(
    #     color='white', edgecolor='black')

    # gdf.plot(ax=ax, color='red')
    # st.pyplot(fig)

    m = leafmap.Map(center=[38.6, -90.3], zoom=11.7)
    # in_shp = "https://github.com/giswqs/leafmap/raw/master/examples/data/countries.zip"
    # in_shp = "countries.zip"
    root = os.path.abspath(os.curdir)
    in_shp = f"{root}/data/st_loius/boundary_proj_shp.shp"
    
    # in_shp = f"{url}/antarctic_ice_edge.json"
    # antarctic_ice_shelf_topo = f"{url}/antarctic_ice_shelf_topo.json"
    
    m.add_shp(in_shp, "St Loius")
    folium.TileLayer('Mapbox Bright').add_to(my_map)
    # m.add_gdf(gdf, layer_name="New York boroughs", fill_colors=["red", "green", "blue"])
    # st.write(in_shp)
    m.to_streamlit(height=700)

