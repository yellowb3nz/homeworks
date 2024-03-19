# Задание 1
num_rows = int(input("Введите количество строк для треугольника Паскаля: "))

triangle = []

for i in range(num_rows):
    row = [1]  # Начало каждой отдельной строки - единица
    if triangle:
        last_row = triangle[-1]  # Последняя строка треугольника
        row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])  # Добавление суммы пар чисел из предыдущей строки группированием
        row.append(1)  # Конец каждой отдельной строки - единица
    triangle.append(row)

count = 3
count += num_rows//10 # Костыль для адекватных отступов ;D (работает до nuw_rows <= 21)

for row in triangle:
    print(' '.join(map(str, row)).center(len(triangle[-1])*count)) # Делаю список row строкой и ровняю её по центру
 

# Задание 2

# num_rows = int(input("Введите количество строк для треугольника Паскаля: "))

# triangle = []

# for i in range(num_rows):
#     row = [1]  # Начало каждой отдельной строки - единица
#     if triangle:
#         last_row = triangle[-1]  # Последняя строка треугольника
#         row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])  # Добавление суммы пар чисел из предыдущей строки группированием
#         row.append(1)  # Конец каждой отдельной строки - единица
#     triangle.append(row)

# count = 3
# count += num_rows//10 # Для адекватных отступов (работает нормально до num_rows <= 21)

# for row in triangle:
#     for i in range(len(row)):
#             if row[i] >= 1000:
#                  if row[i]%2 == 0:
#                       row[i] = '    '
#             elif row[i] >= 100:
#                  if row[i]%2 == 0:
#                       row[i] = '   '                                # Замена всех четных значений на пропуск,
#             elif row[i] >= 10:                                      # для образование треугольника Серпинского
#                 if row[i]%2 == 0:
#                     row[i] = '  '
#             else:
#                  if row[i]%2 == 0:
#                       row[i] = ' '
#     print(' '.join(map(str,row)).center(len(triangle[-1])*count))