# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import (
    get_country_coords,
    save_csv,
)

# dropdown box for selecting country

st.title("Plots 🌎")

le_df = pd.read_csv("./edu_datasets/life_expectancy_years.csv")

countries = le_df["Country"].unique()
# Create a list of countries
# countries = ['South Korea','Argentina']
indices = [
    "Primary Education",
    "Lower Secondary Education",
    "Higher Secondary Education",
    "College Completion",
    "GDP per Capita",
    "Life Expectancy",
    "Total Fertility Rate",
    "Years",
]

col1, col2 = st.columns(2)

cleaned_indices ={
    "pri_edu" : "Primary Education",
    "ls_edu" : "Lower Secondary Education",
    "hs_edu" : "Higher Secondary Education",
    "clg_comp" : "College Completion",
    "gdp" : "GDP per Capita",
    "le" : "Life Expectancy",
    "tfr" : "Total Fertility Rate",
    "years" : "Years",
    
}


params = st.experimental_get_query_params()
selected_countries = params.get("c", countries)
selected_countries = selected_countries[0].split(",")
selected_x, selected_y = indices[0], indices[1]
try:
    selected_x = cleaned_indices[params.get("x", indices)[0]]
except:
    pass

try:
    selected_y = cleaned_indices[params.get("y", indices)[0]]
except:
    pass


try:
    start_year = params.get("sy", 1960)[0]
except:
    start_year = 1960
try:
    end_year = params.get("ey", 2015)[0]
except:
    end_year = 2015


# Add a dropdown box to select a country
selected_countries = st.multiselect("Select Countries", countries, selected_countries)

selected_y = col1.selectbox("Select y axis", indices, index=indices.index(selected_y))
selected_x = col2.selectbox("Select x axis", indices, index=indices.index(selected_x))
selected_years = st.slider("Select years", 1960, 2015, (int(start_year), int(end_year)))

# plot the line chart using Matplotlib
fig, ax = plt.subplots()
country_coords = None
for selected_country in selected_countries:
    country_coords = get_country_coords(selected_country, selected_x, selected_y,selected_years)
    ax.plot(country_coords["x"], country_coords["y"], label=selected_country)

ax.set_xlabel(selected_x)
ax.set_ylabel(selected_y)
ax.set_title(f"{selected_x} vs {selected_y}")
ax.legend()

if country_coords is not None:
    col1, col2  = st.columns(2)
    file_name   = f"{selected_x[:3]}_{selected_y[:3]}"

    csv_snippet = save_csv(selected_countries, selected_x, selected_y, selected_years)
    with open("chart.csv", "rb") as f:
        data_bytes = f.read()
        col1.download_button(
            label       = "Download Data 💿",
            data        = data_bytes,
            file_name   = f"{file_name}.csv",
            mime        = "text/csv",
        )

    fig.savefig("chart.png")
    with open("chart.png", "rb") as f:
        image_bytes = f.read()
        col2.download_button(
            label       = "Download Graph 📈",
            data        = image_bytes,
            file_name   = f"{file_name}.png",
            mime        = "image/png",
        )
# display the chart in Streamlit app
st.pyplot(fig)


# hide the text to a dropdown
st.markdown(
    """
    <details>
    <summary style="font-size: 20px">Passing Input Parameters from URL</summary>
    <br>
    <p style="font-size: 15px">
    Passing the following query parameters to the URL will pre-select countries and indices:
    
    - `c`: comma-separated list of countries
    - `x`: x-axis index
    - `y`: y-axis index
    - `sy`: start year
    - `ey`: end year
    
    The following indices are available:
    - `pri_edu`: Primary Education
    - `ls_edu`: Lower Secondary Education
    - `hs_edu`: Higher Secondary Education
    - `clg_comp`: College Completion
    - `gdp`: GDP per Capita
    - `le`: Life Expectancy
    - `tfr`: Total Fertility Rate
    - `years`: Years
    
    Example:  
    **_?c=South Korea,Argentina&x=pri_edu&y=le&sy=1960&ey=2015_**
    
    The following url is used to generate for **Primary Education vs Life Expectancy for South Korea and Argentina from 1960 to 2015**
   
    </p>
    </details>
    """,
    unsafe_allow_html=True,
)

# st.write(
#     "Passing the following query parameters to the URL will pre-select countries and indices:" 
# )
# st.markdown(
#     """
#     - `c`: comma-separated list of countries
#     - `x`: x-axis index
#     - `y`: y-axis index
#     - `sy`: start year
#     - `ey`: end year
#     """
# )

# st.markdown(
#     """
#     The following indices are available:
#     - `pri_edu`: Primary Education
#     - `ls_edu`: Lower Secondary Education
#     - `hs_edu`: Higher Secondary Education
#     - `clg_comp`: College Completion
#     - `gdp`: GDP per Capita
#     - `le`: Life Expectancy
#     - `tfr`: Total Fertility Rate
#     - `years`: Years
#     """
# )

# st.markdown(
#     """
#     Example:  
#     **_?c=South Korea,Argentina&x=pri_edu&y=le&sy=1960&ey=2015_**
    
#     The following url is used to generate for **Primary Education vs Life Expectancy for South Korea and Argentina from 1960 to 2015**
#     """
# )


