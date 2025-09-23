import pandas as pd

df = pd.read_csv("Meteorite_Landings.csv")

df = df.rename(columns={
    "name": "Meteorite Name",
    "mass": "Mass_g",
    "year": "Year"
})

df_new = df[["Meteorite Name", "Mass_g", "Year"]]

print(df_new.head())