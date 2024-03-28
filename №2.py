import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data1.csv')
selected_data = data.iloc[:, [0, 3, 17]]

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))

ax1.plot(selected_data.iloc[:, 0], label='Столбец 1')
ax1.set_title('Данные из столбца 1')
ax1.set_xlabel('Индекс')
ax1.set_ylabel('Время')
ax1.legend()

ax2.plot(selected_data.iloc[:, 1], label='Столбец 4')
ax2.set_title('Данные из столбца 4')
ax2.set_xlabel('Индекс')
ax2.set_ylabel('Положение дроссельной \n заслонки (%)')
ax2.legend()

ax3.plot(selected_data.iloc[:, 2], label='Столбец 18')
ax3.set_title('Данные из столбца 18')
ax3.set_xlabel('Индекс')
ax3.set_ylabel('Часовой расход \n топлива (л\час)')
ax3.legend()

plt.subplots_adjust(hspace=1)

correlation_matrix = selected_data.corr()
plt.figure(figsize=(6, 4))
plt.title('Корреляция между столбцами')
plt.imshow(correlation_matrix, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Коэффициент корреляции')
plt.xticks(range(len(correlation_matrix)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix)), correlation_matrix.columns)
plt.show()
