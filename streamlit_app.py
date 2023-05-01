import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import get_country_coords

# dropdown box for selecting country

st.title('Plots')

# Create a list of countries
countries = ['South Korea','Argentina']
indices = ['Primary Education', 'Lower Secondary Education', 'Higher Secondary Education', 'College Completion', 'GDP per Capita', 'Life Expectancy', 'Total Fertility Rate','Years']

col1, col2 = st.columns(2)
# Add a dropdown box to select a country
selected_country_1 = col1.selectbox('Select a country 1', countries)
selected_country_2 = col2.selectbox('Select a country 2', countries)

selected_x = col1.selectbox('Select x axis', indices)
selected_y = col2.selectbox('Select y axis', indices)




country_1_coords = get_country_coords(selected_country_1, selected_x, selected_y)
country_2_coords = get_country_coords(selected_country_2, selected_x, selected_y)

# plot the line chart using Matplotlib
fig, ax = plt.subplots()
ax.plot(country_1_coords['x'], country_1_coords['y'], label=selected_country_1)
ax.plot(country_2_coords['x'], country_2_coords['y'], label=selected_country_2)
ax.set_xlabel(selected_x)
ax.set_ylabel(selected_y)
ax.set_title(f'{selected_x} vs {selected_y}')
ax.legend()

# display the chart in Streamlit app
st.pyplot(fig)
