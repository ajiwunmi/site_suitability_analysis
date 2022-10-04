import pandas as pd
import numpy as np
import pydeck as pdk
import streamlit as st


# def app():

#     st.title("Deck Map")

#     df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

#     st.pydeck_chart(pdk.Deck(
#             map_style=None,
#             initial_view_state=pdk.ViewState(
#                 latitude=37.76,
#                 longitude=-122.4,
#                 zoom=11,
#                 pitch=50,
#             ),
#             layers=[
#                 pdk.Layer(
#                     'HexagonLayer',
#                     data=df,
#                     get_position='[lon, lat]',
#                     radius=200,
#                     elevation_scale=4,
#                     elevation_range=[0, 1000],
#                     pickable=True,
#                     extruded=True,
#                 ),
#                 pdk.Layer(
#                     'ScatterplotLayer',
#                     data=df,
#                     get_position='[lon, lat]',
#                     get_color='[200, 30, 0, 160]',
#                     get_radius=200,
#                 ),
#             ],
#         ))

# def app():
#     data = pd.DataFrame({
#         'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
#         'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
#         'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
#     })

#     # Adding code so we can have map default to the center of the data
#     midpoint = (np.average(data['lat']), np.average(data['lon']))

#     st.pydeck_chart(
#             viewport={
#                 'latitude': midpoint[0],
#                 'longitude':  midpoint[1],
#                 'zoom': 4
#             },
#             layers=[{
#                 'type': 'ScatterplotLayer',
#                 'data': data,
#                 'radiusScale': 250,
#    'radiusMinPixels': 5,
#                 'getFillColor': [248, 24, 148],
#             }]
#         )

def app():

    st.title("Deck Map")
    # label 'Chicago', 'Minneapolis', 'Louisville', 'Topeka', 
    # lat 41.868171, 44.979840,  38.257972, 39.030575,
    #log -87.667458, -93.272474, -85.765187,  -95.702548, 
    data = pd.DataFrame({
        'awesome cities' : ['St louis'], 
        'lat' : [ 38.627003],
        'lon' : [-90.199402]
    })

    # Adding code so we can have map default to the center of the data
    midpoint = (np.average(data['lat']), np.average(data['lon']))

    st.pydeck_chart(pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=midpoint[0],
                longitude=midpoint[1],
                zoom=11,
                pitch=5,
            ),
            layers=[
                pdk.Layer(
                    'ScatterplotLayer',
                    data=data,
                    get_position='[lon, lat]',
                    get_color='[200, 30, 0, 160]',
                    get_radius=200,
                ),
            ],
        ))

