import random

#Задание 1
# numbers = []
# for i in range(7):
#     numbers.append(random.randint(0,9))

# print("Входные данные:", numbers)

# setted_numbers = set(numbers)
# print("Выходные значения:", len(setted_numbers))

#Задание 2
# numbers1 = set()
# numbers2 = set()

# for i in range(3):
#     numbers1.add(random.randint(0,9))

# for i in range(10):
#     numbers2.add(random.randint(0,9))

# print(f"Входные данные: \n{numbers1} \n{numbers2}")

# if numbers1 < numbers2:
#     print("Выходные значения: True!")
# else:
#     print("Выходные значения: False!")

#Задание 3
# def play_cities_game(max_cities):
#     cities = set()

#     while True:
#         city = input("Введите название города: ")

#         if city.lower() == "выход":
#             print("Игра завершена.")
#             break

#         if city in cities:
#             print("Такой город уже был назван. Попробуйте другой.")
#             continue

#         cities.add(city)

#         if len(cities) > max_cities:
#             print(f"Вы назвали уже {len(cities)} городов, что превышает максимальное число городов в игре. Игра окончена.")
#             break

#         flag_letter = ['ь', 'ы', 'ъ']
#         last_letter = city[-1].lower()
#         if last_letter in flag_letter:
#             last_letter = city[-2].lower()

#         next_city = input(f"Введите название города, начинающегося на букву '{last_letter}': ")

#         if next_city.lower() == "выход":
#             print("Игра завершена.")
#             break

#         if next_city[0].lower() != last_letter:
#             print(f"Название города должно начинаться на букву '{last_letter}'. Попробуйте еще раз.")
#             continue

#         if next_city in cities:
#             print("Такой город уже был назван. Попробуйте другой.")
#             continue

#         cities.add(next_city)
#         print(f"Введите название города, начинающегося на букву\
#                '{next_city[-1] if next_city[-1] not in flag_letter else next_city[-2]}': ")

# play_cities_game(int(input("Введите максимальное количество городов: ")))

#Задание 4
# def count_occurrences(input_string):
#     words = input_string.split()
#     word_count = {}
#     result = []

#     for word in words:
#         if word not in word_count:
#             word_count[word] = 0
#             result.append(0)
#         else:
#             word_count[word] += 1
#             result.append(word_count[word])

#     return result

# input_string = str(input("Введите строку: "))
# words = input_string.split()
# word_count = {}
# result = []

# for word in words:
#     if word not in word_count:
#         word_count[word] = 0
#         result.append(0)
#     else:
#         word_count[word] += 1
#         result.append(word_count[word])

# print(result)

#Задание 5
# def count_items_purchased(n):
#     purchases = {}

#     for _ in range(n):
#         record = input("Введите запись о покупке в формате ID Покупателя Товар(Пробел выглядит как _) Количество: ").split()
#         customer_id = int(record[0])
#         item_name = record[1]
#         quantity = int(record[2])

#         if customer_id not in purchases:
#             purchases[customer_id] = []

#         purchases[customer_id].append((item_name, quantity))

#     for customer_id, items in purchases.items():
#         print(f"Покупатель с ID {customer_id} приобрел следующие товары:")
#         for item in items:
#             print(f"{item[0]}: {item[1]} шт.")

# n = int(input("Введите количество записей о покупках: "))
# count_items_purchased(n)

#Задание 6
from collections import Counter

def print_words(text):
    text = text.lower()
    for special_symbol in '.,;:-?!()[]{}"\'':
        text = text.replace(special_symbol, ' ')
    words = text.split()

    word_counts = Counter(words)

    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_words:
        print(word)

text = input("Текст: ")
print_words(text)