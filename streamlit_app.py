import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import get_country_coords

# dropdown box for selecting country

st.title('Plots')

le_df = pd.read_csv("./edu_datasets/life_expectancy_years.csv")

countries = le_df['Country'].unique()
# Create a list of countries
# countries = ['South Korea','Argentina']
indices = ['Primary Education', 'Lower Secondary Education', 'Higher Secondary Education', 'College Completion', 'GDP per Capita', 'Life Expectancy', 'Total Fertility Rate','Years']

col1, col2 = st.columns(2)
# Add a dropdown box to select a country
selected_countries = st.multiselect('Select Countries', countries )
selected_x = col1.selectbox('Select x axis', indices)
selected_y = col2.selectbox('Select y axis', indices)

# plot the line chart using Matplotlib
fig, ax = plt.subplots()
for selected_country in selected_countries:
    country_coords = get_country_coords(selected_country, selected_x, selected_y)
    ax.plot(country_coords['x'], country_coords['y'], label=selected_country)

ax.set_xlabel(selected_x)
ax.set_ylabel(selected_y)
ax.set_title(f'{selected_x} vs {selected_y}')
ax.legend()

# display the chart in Streamlit app
st.pyplot(fig)
st.write("**Note** : The graphs are plotted for data collected between the years 1960-2015")
