import pandas as pd

root = "./edu_datasets/" 
datasets_path = {
                    "Primary Education"               :  root+ "20-24-Primary_fin.csv",
                    "Lower Secondary Education"       :  root+ "20-24-Lower_Secondary_fin.csv",
                    "Higher Secondary Education"      :  root+ "20-24-Higher_Secondary_fin.csv",
                    "College Completion"              :  root+ "College_comp.csv",
                    "Total Fertility Rate"            :  root+ "children_per_woman_total_fertility.csv",
                    "GDP per Capita"                  :  root+ "gdppercapita_us_inflation_adjusted.csv",
                    "Life Expectancy"                 :  root+ "life_expectancy_years.csv",
                    "Years"                           :  root+ "years.csv",
                    "india_tfr"                       :  root+ "India/TFR.csv"
                    
                }

def get_country_coords(country, x, y):
    
    df_1 = pd.read_csv(datasets_path[x])
    df_2 = pd.read_csv(datasets_path[y])
    
    df_1 = df_1[df_1['Country'] == country]
    df_2 = df_2[df_2['Country'] == country]
    
    df_1 = df_1.drop(['Country'], axis=1)
    df_2 = df_2.drop(['Country'], axis=1)
    
    df_1 = df_1.T
    df_2 = df_2.T
    
    df_3 = df_1.merge(df_2, left_index=True, right_index=True)
    df_3.columns = ['x', 'y']
    df_3.dropna(inplace=True)
    df_3.reset_index(drop=True, inplace=True)
    
    return df_3