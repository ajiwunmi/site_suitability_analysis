import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import leafmap.foliumap as leafmap
from folium.plugins import Draw
from apps.utils import geomap



def app():
    st.title("Home")
    st.subheader("Site Suitability Analysis")
    st.markdown(
        """
            Location suitability analysis is an analysis method that overlaps different data and transfers them into a scale. After sum up those scores from different layers, the places have higher score are considered as better locations.
            Identifying the best place for something—where to land an emergency helicopter, for example—can be complicated. Suitability modeling is a common approach to answering this question, factoring in multiple variables of varying importance to identify locations that best meet established criteria for a site.
            Suitability modeling can solve a variety of problems. 
            Examples include:

            Where to site a new housing development
            Identifying potential wildlife habitat areas
            Identifying optimum routes (i.e. cross-country mobility)
            Where to locate firefighting crews to best fight fires in the dry season
            Where to deploy troops in a military operation
            Where to locate a new ski area

        """)

    # m = leafmap.Map(locate_control=True)
    # m.add_basemap("ROADMAP")
    # m.to_streamlit(height=700)
    
    
    # m = leafmap.Map(center=[0, 0], zoom=2)
    # in_shp = 'https://github.com/giswqs/leafmap/raw/master/examples/data/countries.zip'
    # m.add_shp(in_shp, layer_name="Country")
    # m.to_streamlit(height=700)

    # request St Louis data from OSM

    
    location = geomap.load_location()
    m = folium.Map(location=location, width =800, height=400,zoom_start=11)
    # m = leafmap.Map(location=location, width =800, height=400,zoom_start=10)
   
    # st.write(location)
    folium.Marker(location, popup="St. Louis").add_to(m)

    folium.Marker(location, popup="St. Louis").add_to(m)
    Draw(export=True).add_to(m)
    st_data = st_folium(m, width = 725)

    # ##########################################################33333  
    


