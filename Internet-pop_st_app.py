import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy


#to run file make sure you are in the correct env both bottom corner and usnig conda
#env list - restart vs code if need be
#make sure you are in file directory cd ...
#streamlit run internet-pop_st_app.py


# First some MPG Data Exploration
df = pd.read_csv("./data/raw/share-of-individuals-using-the-internet.csv")

# Add title and header
st.title("Internet use % population")
st.header("across years")

with open('../data/countries.geojson') as response:
    countries = json.load(response)


if st.checkbox("show DataFrame"):
    st.dataframe(data=df)


yr=2017
df_yr=df[df['Year']==yr]
df_yr = df_yr.rename(columns={'Individuals using the Internet (% of population)': 'population_internet'})
# Drop rows with NaN values in the 'Code' column
df_yr = df_yr.dropna(subset=['Code'])

with open('../data/countries.geojson') as response:
    countries = json.load(response)

fig = px.choropleth(df_yr, geojson=countries, locations='Code', featureidkey="properties.ISO_A3",
                    color='population_internet', color_continuous_scale="Viridis",
                    range_color=(0, 100),
                    labels={'Population':'Population'},
                    title="Population Map")

fig.update_geos(fitbounds="locations", visible=True)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()