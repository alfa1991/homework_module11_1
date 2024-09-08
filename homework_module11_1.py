import requests
import numpy as np
import matplotlib.pyplot as plt

# Выполнение GET-запроса на сайт
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг JSON-ответа
    data = response.json()
    print("Полученные данные:")
    print(data)
else:
    print(f"Ошибка запроса: {response.status_code}")



# Создание массива чисел
array = np.array([1, 2, 3, 4, 5])

# Выполнение математических операций
multiplied_array = array * 10
mean_value = np.mean(array)
std_deviation = np.std(array)

# Вывод результатов
print(f"Исходный массив: {array}")
print(f"Умноженный массив: {multiplied_array}")
print(f"Среднее значение: {mean_value}")
print(f"Стандартное отклонение: {std_deviation}")



# Данные для визуализации
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Построение графика
plt.plot(x, y, label='sin(x)')
plt.title('График функции sin(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# Показ графика
plt.show()

