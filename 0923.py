import matplotlib.pyplot as plt
import numpy as np

# np.random.seed(42)
# categories = [f"Cat{i}" for i in range(1, 9)]  # 8 категорій
# values = np.random.randint(5, 50, size=len(categories))

# fig, axs = plt.subplots(3, 2, figsize=(16, 14))  # 3 ряди, 2 колонки
# fig.suptitle("Барчарти з різними налаштуваннями", fontsize=20, fontweight='bold')

# axs[0, 0].bar(categories, values, color='skyblue', width=0.6, label="Random Data")
# axs[0, 0].set_title("Базові стовпці")
# axs[0, 0].set_xlabel("Категорії")
# axs[0, 0].set_ylabel("Значення")
# axs[0, 0].legend()

# colors = np.random.choice(['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'pink', 'brown'], size=len(categories))
# axs[0, 1].bar(categories, values, color=colors, edgecolor='black', linewidth=1.5, alpha=0.7)
# axs[0, 1].set_title("Кольорові з рамками")

# axs[1, 0].bar(categories, values, color='purple')
# axs[1, 0].set_title("Стовпці з сіткою")
# axs[1, 0].set_xlabel("Категорії")
# axs[1, 0].set_ylabel("Значення")
# axs[1, 0].grid(axis='y', linestyle='--', alpha=0.6)

# axs[1, 1].barh(categories, values, color='cyan', edgecolor='black')
# axs[1, 1].set_title("Горизонтальні стовпці")
# axs[1, 1].set_xlabel("Значення")
# axs[1, 1].grid(axis='x', linestyle=':', alpha=0.7)

# values1 = np.random.randint(10, 40, size=len(categories))
# values2 = np.random.randint(10, 40, size=len(categories))
# x = np.arange(len(categories))

# axs[2, 0].bar(x - 0.2, values1, width=0.4, color='blue', label='Група 1')
# axs[2, 0].bar(x + 0.2, values2, width=0.4, color='green', label='Група 2')
# axs[2, 0].set_xticks(x)
# axs[2, 0].set_xticklabels(categories, rotation=30)
# axs[2, 0].set_title("Порівняння двох груп")
# axs[2, 0].set_xlabel("Категорії")
# axs[2, 0].set_ylabel("Значення")
# axs[2, 0].legend()

# groups = 4
# width = 0.18
# x = np.arange(len(categories))
# for i in range(groups):
#     vals = np.random.randint(5, 50, size=len(categories))
#     axs[2, 1].bar(x + (i - groups/2)*width, vals, width=width, label=f'Група {i+1}', alpha=0.8)

# axs[2, 1].set_xticks(x)
# axs[2, 1].set_xticklabels(categories, rotation=30)
# axs[2, 1].set_title("Порівняння кількох груп")
# axs[2, 1].set_xlabel("Категорії")
# axs[2, 1].set_ylabel("Значення")
# axs[2, 1].legend()

# plt.tight_layout(rect=[0, 0, 1, 0.97])
# plt.show()


# categories = ['A', 'B', 'C', 'D', 'E']
# values = [10, 20, 15, 30, 25]
# colors = ['red', 'blue', 'green', 'orange', 'purple']

# plt.bar(categories, values, color=colors)


# plt.xlabel("Категорії")
# plt.ylabel("Значення")
# plt.title("Діаграма з різнокольоровими стовпцями")

# plt.show()



# ___________________________________________________________________________



# athletes = ['A', 'B', 'C']
# medals = [5, 10, 7]

# plt.bar(athletes, medals, color='gold')

# for i, value in enumerate(medals):
#     plt.text(i, value + 0.5, str(value), ha='center')

# plt.xlabel("Спортсмени")
# plt.ylabel("Кількість медалей")
# plt.title("Медалі спортсменів")

# plt.show()



# ___________________________________________________________________________



# countries = ['США', 'Канада', 'Мексика', 'Бразилія']
# gdp = [21.43, 1.74, 1.22, 2.05]

# plt.barh(countries, gdp, color='lightblue')


# plt.xlabel('ВВП Трильйони долларів')
# plt.ylabel('Країни')
# plt.title('ВВП Країн')

# plt.show()



# ___________________________________________________________________________


# sizes = [30, 30, 20, 20]
# labels = ['A', 'B', 'C', 'D']


# plt.pie(sizes, labels=labels)
# plt.title('Кругова Діаграма')
# plt.show()


# ___________________________________________________________________________


# sizes = [50, 25, 15, 10]
# labels = ['Продажі', 'Інвестиції', 'Ліцензії', 'Інше']

# plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# plt.title("Джерела доходу")
# plt.show()


# ___________________________________________________________________________


# sizes = [40, 35, 15, 10]
# labels = ['Оренда', 'Зарплати', 'Маркентинг', 'Інше']
# explode = [0.1, 0, 0, 0]

# plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, startangle=90)
# plt.title('Структура Витрат')
# plt.show()



# ___________________________________________________________________________
