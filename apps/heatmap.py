import streamlit as st
import leafmap.foliumap as leafmap
from apps.utils import geomap, root
import folium
import geopandas as gpd


# import map_location.load_location as location 


def app():
    # st.title('')
    st.subheader('The Input Attributes')
    datashapes = {'boundary':'boundary_proj_shp.shp',
                  'college': 'financial_institution.shp',
                  'highway':'primary_road_proj.shp',
                  'health':'health_facility_proh_shp.shp',
                  'shopping':'Shopping centers.shp',
                  }

    # st.write(datashapes)
    col1, col2=   st.columns([1,4])
    
    with col1:
       
        boundary= st.checkbox('Administrative Boundary')
        college = st.checkbox('University/College')
        highway = st.checkbox('Highway')
        health = st.checkbox('Health Care Facility')
        shopping = st.checkbox('Shopping Centers')

        # st.write(boundary)

    with col2:
        shapefile = state_shp =False

        loc  = geomap.load_location()
        m = leafmap.Map(center=loc, zoom=11)
        style = {
            "stroke": True,
            "color": "#0000FF",
            "weight": 2,
            "opacity": 1,
            "fill": True,
            "fillColor": "#0000ff",
            "fillOpacity": 0.1,
        }

        if(boundary):
            shapefile = datashapes['boundary']
            state_shp =f"{root.path()}{shapefile}"
            m.add_shp(state_shp , layer_name="Boundary",style=style)
        
        if(college):
            shapefile = datashapes['college']
            state_shp =f"{root.path()}{shapefile}"
            m.add_shp(state_shp , layer_name="Boundary",style=style)
        
        if(highway):
            style['color'] = '#FFFF00'
            shapefile = datashapes['highway']
            state_shp =f"{root.path()}{shapefile}"
            m.add_shp(state_shp , layer_name="Boundary",style=style)

        if(health):
            style['fillColor'] = '#00FF00'
            shapefile = datashapes['health']
            state_shp =f"{root.path()}{shapefile}"
            m.add_shp(state_shp , layer_name="Boundary",style=style)

        if(shopping):
            shapefile = datashapes['shopping']
            state_shp =f"{root.path()}{shapefile}"
            m.add_shp(state_shp , layer_name="Boundary",style=style)

        # if(shapefile):   
            
        # earthquake = gpd.read_file(state_geo)
        # st.write(earthquake.head())
        
        # m.add_geojson(state_geo, layer_name="boundary", style=style)
        
           
        m.to_streamlit(height=500)
            
    

    
    # st.title("Attributes")
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
    # state_geo = f"{url}/us-states.json"
    

    

   
    

    
   
