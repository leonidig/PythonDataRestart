import numpy as np
import matplotlib.pyplot as plt


plt.style.use("seaborn-v0_8")
fig, axs = plt.subplots(4, 2, figsize=(16, 12))
fig.suptitle("Демонстрація кругових діаграм", fontsize=20, fontweight="bold")

# TASK - 1
sizes1 = [30, 30, 20, 20]
labels1 = ['A', 'B', 'C', 'D']

axs[0,0].pie(sizes1, labels=labels1)
axs[0,0].set_title("Розподіл категорій")

# TASK - 2
sizes2 = [50, 25, 15, 10]
labels2 = ['Продажі', 'Інвестиції', 'Ліцензії', 'Інше']

axs[1,0].pie(sizes1, labels=labels1, autopct='%1.1f%%')
axs[1,0].set_title("Джерела доходу")

# TASK - 3
sizes3 = [40, 35, 15, 10]
labels3 = ['Оренда', 'Зарплати', 'Маркетинг', 'Інше']

axs[2,0].pie(sizes3, labels=labels3, colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'])
axs[2,0].set_title("Розподіл витрат")


# TASK - 4
sizes4 = [60, 25, 10, 5]
labels4 = ['A', 'B', 'C', 'D']
explode = [0.1, 0, 0.5, 0.3]

axs[3,0].pie(sizes4, labels=labels4, explode=explode, autopct='%1.1f%%')
axs[3,0].set_title("Зсув сегментів")


# TASK - 5
sizes5 = [50, 30, 15, 5]
labels5 = ['Категорія 1', 'Категорія 2', 'Категорія 3', 'Категорія 4']

axs[0,1].pie(sizes5, labels=labels5, autopct='%1.1f%%', startangle=90)
axs[0,1].set_title("Розподіл категорій")

# TASK - 6
sizes6 = [30, 45, 15, 10]
labels6 = ['Тип A', 'Тип B', 'Тип C', 'Тип D']

axs[1,1].pie(sizes6, labels=labels6, autopct='%1.1f%%', shadow=True)
axs[1,1].set_title("Транспортні засоби")

# TASK - 7
sizes = [25, 35, 20, 20]
labels = ['A', 'B', 'C', 'D']

axs[2,1].pie(sizes, labels=labels, autopct='%1.1f%%', wedgeprops={'width': 0.4})
axs[2,1].set_title("Кільцева діаграма")


# TASK - 8
sizes8 = [60, 20, 15, 5]
labels8 = ['A', 'B', 'C', 'D']

axs[3,1].pie(sizes8, labels=labels8, autopct='%.0f')
axs[3,1].set_title("Розподіл сегментів")

plt.show()