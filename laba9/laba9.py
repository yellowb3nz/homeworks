import numpy as np
from scipy.stats import multivariate_normal

# Задание 1
# matrix = """
# 3,4,17,-3
# 5,11,-1,6
# 0,2,-5,8"""
# with open("C:\\Users\\Danya\\Desktop\\laba9\\text.txt", "w") as f:
#     f.write(matrix)

# matrix = np.genfromtxt("C:\\Users\\Danya\\Desktop\\laba9\\text.txt", delimiter=',')
# Sum = int(np.sum(matrix))
# Maximum = int(np.max(matrix))
# Minimum = int(np.min(matrix))

# print("Сумма", Sum)
# print("Наибольший элемент", Maximum)
# print("Наименьший элемент", Minimum)

# Задание 2
# x = np.array([2, 2, 2, 3, 3, 3, 5])
# unique_values, counts = np.unique(x, return_counts=True)

# print(unique_values, counts)

# Задание 3
# arr = np.random.normal(size=(10, 4))

# Minimum = np.min(arr)
# Maximum = np.max(arr)
# Mean = np.mean(arr)
# Deviation = np.std(arr)
# FirstFive = arr[:5, :]

# print("Наименьший элемент", Minimum)
# print("Наибольший элемент", Maximum)
# print("Среднее", Mean)
# print("Отклонение:", Deviation)
# print("Первые пять сохраненных --->\n", FirstFive)

# Задание 4
# x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
# ZeroElem = np.where(x[:-1] == 0)[0]
# MaxAfterZeroElem = np.max(x[ZeroElem + 1])

# print("Максимальный элемент в векторе x среди элементов, перед которыми стоит нулевой:", MaxAfterZeroElem)

# Задание 5
# def multivariate_normal_logpdf(X, m, C):
#     D = m.shape[0]
#     det_C = np.linalg.det(C)
#     inv_C = np.linalg.inv(C)
#     norm_const = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C)
#     X_m = X - m
#     exponent = -0.5 * np.sum(X_m @ inv_C * X_m, axis=1)
#     log_pdf = norm_const + exponent
#     return log_pdf

# m = np.array([1, 2])
# C = np.array([[2, 1], [1, 4]])
# X = np.array([[1, 2], [3, 4]])
# result_custom = multivariate_normal_logpdf(X, m, C)
# print("Результат собственной функции:", result_custom)

# result_scipy = multivariate_normal(m, C).logpdf(X)
# print("Результат scipy.stats.multivariate_normal:", result_scipy)

# Задание 6
# a = np.arange(16).reshape(4, 4)
# print("Исходный массив a:")
# print(a)

# a[[1, 3]] = a[[3, 1]]

# print("\nМассив a после замены строк 1 и 3:")
# print(a)


# Задание 7
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris = np.genfromtxt(url, delimiter=',', dtype='object')
# species_column = iris[:, 4]

# unique_species, counts = np.unique(species_column, return_counts=True)

# print("Уникальные значения в 'species' --->", unique_species)
# print("Количество каждого уникального значения --->", counts)

# Задание 8
# arr = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
# nonzero = np.nonzero(x)[0]
# print("Индексы ненулевых --->", nonzero)