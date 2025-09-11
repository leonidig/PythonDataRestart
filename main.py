import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Meteorite_Landings.csv')
# print(df.head(10))
# print(df.info())
# print(df.columns)

# a = len(df)
# print(a)
# print(df.describe())
# print(df.shape)
# print(df[["mass", "year"]])



# _______________________________________________________________________________



# category_counts = df['fall'].value_counts()
# print("Розподіл за типом виявлення:")
# print(category_counts)

# meteorite_types = df['recclass'].value_counts().head(10)
# print("\nНайпоширеніші типи метеоритів:")
# print(meteorite_types)

# plt.figure(figsize=(10, 6))
# meteorite_types.plot(kind='bar')
# plt.title('Топ-10 найпоширеніших типів метеоритів')
# plt.xlabel('Тип метеорита')
# plt.ylabel('Кількість')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()



# _______________________________________________________________________________



