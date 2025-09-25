import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# data = {
#     'Date': [
#         '2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03',
#         '2023-01-04', '2023-01-04', '2023-01-05', '2023-01-05', '2023-01-06',
#         '2023-02-01', '2023-02-01', '2023-02-02', '2023-02-02', '2023-02-03',
#         '2023-02-04', '2023-02-04', '2023-02-05', '2023-02-05', '2023-02-06'
#     ],
#     'Product': [
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch',
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch',
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch',
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch'
#     ],
#     'Category': [
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories',
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories',
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories',
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories'
#     ],
#     'Region': [
#         'North', 'South', 'East', 'West', 'North',
#         'South', 'East', 'West', 'North', 'South',
#         'East', 'West', 'North', 'South', 'East',
#         'West', 'North', 'South', 'East', 'West'
#     ],
#     'Sales': [
#         50, 30, 20, 100, 40,
#         60, 25, 35, 80, 45,
#         55, 40, 25, 90, 50,
#         65, 35, 30, 100, 55
#     ],
#     'Revenue': [
#         25000, 45000, 10000, 10000, 20000,
#         30000, 37500, 17500, 8000, 22500,
#         27500, 60000, 12500, 9000, 25000,
#         32500, 52500, 15000, 10000, 27500
#     ]
# }

# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'])
# sns.countplot(data=df, x='Category', palette='Set2')

# sns.barplot(data=df, x='Category', y='Revenue', estimator=np.sum, palette='coolwarm')
# plt.title('Сумарний Дохід за Категоріями Продуктів')
# plt.xlabel('Категорія')
# plt.ylabel('Сумарний Дохід (USD)')

# plt.show()


# print(df.head())







df = sns.load_dataset('penguins')

print(df.head())


# sns.countplot(data=df, x='species')
# plt.title('Кількість пінгвінів за видами')
# plt.xlabel('Вид Пінгвінів')
# plt.ylabel('Кількість Спостережень')
# plt.show()


# sns.countplot(data=df, x='species', hue='sex', palette='muted')
# plt.title('Кількість Пінгвінів за Видами та Статтю')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Кількість Спостережень')
# plt.legend(title='Стать')
# plt.show()


# sns.barplot(data=df, x='species', y='body_mass_g', palette='pastel')
# plt.title('Середня Маса Тіла за Видами Пінгвінів')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Середня Маса Тіла (г)')
# plt.show()


# sns.barplot(data=df, x='species', y='body_mass_g', palette='pastel')
# plt.title('Середня Маса Тіла за Видами Пінгвінів')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Середня Маса Тіла (г)')
# plt.show()


# sns.barplot(data=df, x='species', y='body_mass_g', hue='sex', palette='deep')
# plt.title('Середня Маса Тіла за Видами Пінгвінів та Статтю')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Середня Маса Тіла (г)')
# plt.legend(title='Стать')
# plt.show()


# sns.barplot(data=df, x='species', y='body_mass_g', estimator=np.sum, palette='coolwarm')
# plt.title('Сумарна Маса Тіла за Видами Пінгвінів')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Сумарна Маса Тіла (г)')
# plt.show()


# sns.barplot(data=df, x='species', y='body_mass_g', hue='sex', estimator=np.median, palette='Set1')

# plt.title('Медіанні Маси Тіла за Видами Пінгвінів та Статтю')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Медіанні Маса Тіла (г)')
# plt.legend(title='Стать')

# for p in plt.gca().patches:
#     plt.annotate(format(p.get_height(), '.1f'),
#                  (p.get_x() + p.get_width() / 2, p.get_height()),
#                  ha='center', va='center',
#                  xytext=(0, 5),
#                  textcoords='offset points')

# plt.show()


sns.barplot(data=df, x='species', y='body_mass_g', estimator=np.mean, ci='sd', palette='viridis')
plt.title('Середня Маса Тіла за Видами Пінгвінів з Стандартним Відхиленням')
plt.xlabel('Вид Пінгвіна')
plt.ylabel('Середня Маса Тіла (г)')

for p in plt.gca().patches:
    plt.annotate(format(p.get_height(), '.1f'),
                 (p.get_x() + p.get_width() / 2, p.get_height()),
                 ha='center', va='bottom',
                 xytext=(0, 5),
                 textcoords='offset points')

plt.show()