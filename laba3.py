# Task 1
string = str(input('Введите строку:')) + ' '
newstr = ''

count = 1
for i in range(0, len(string)-1):
    if string[i] == string[i+1]:
        count += 1
    else:
        newstr += string[i]
        if count != 1:
            newstr += str(count)
        count = 1
print(newstr)




# Task 2
# string = 'Y4g2ke3A3BV'
# newstr = ''

# for i in range(0, len(string)):
#     if string[i].isdigit() != 1:
#         newstr += string[i]
#     else:
#         newstr += (string[i-1]*int(string[i]))[:-1]
# print(newstr)




# Task 3
# s = int(input('Введите число от 1 до 1000: '))

# Singles = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
# Specials = ['одиннадцать', 'двенадцать', 'тренадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
#              'семнадцать', 'восемнадцать', 'девятнадцать']
# Doubles = ['', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
# Triples = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
# if s == 1000:
#     print('Тысяча')

# if 1 <= s <= 10:
#     print(Singles[s])

# elif 11 <= s <= 19:
#     print(Specials[s%10-1])

# elif 20 <= s <= 999:
#     triple = s%1000//100
#     double = s%100//10
#     single = s%10
#     special = s%100

#     if 11 <= special <= 19:
#         print(Triples[triple] + ' ' + Specials[special%10-1])

#     elif double == 0 and single != 0:
#         print(Triples[triple] + ' ' + Singles[single])

#     elif double == 0 and single == 0:
#         print(Triples[triple])

#     elif single != 0:
#         print(Triples[triple] + ' ' + Doubles[double-1] + ' ' + Singles[single])

#     else:
#         print(Triples[triple] + ' ' + Doubles[double-1])




# Task 4
# strings = ['abc', 'bcd', 'abc', 'abc', 'dcd']
# occurrences = {}

# for string in strings:
#     if string in occurrences:
#         occurrences[string] += 1
#     else:
#         occurrences[string] = 1

# for string, count in occurrences.items():
#     print(f'{string}: {count}')




# Task 5
# def determinant(matrix):
#     n = len(matrix)
    
#     if n == 1:
#         return matrix[0][0]
    
#     det = 0
#     for i in range(n):
#         minor = [row[:i] + row[i+1:] for row in matrix[1:]]
#         det += ((-1) ** i) * matrix[0][i] * determinant(minor)           #Если определитель матрицы равен 0, то ЛЗ
#     return det                                                           #Иначе ЛНЗ


# # Пример матрицы
# matrix = [[1, 0, 0],
#           [0, 1, 2],
#           [0, 0, 1]]

# det = determinant(matrix)
# if det == 0:
#     print('Линейно зависимая матрица')
# else:
#     print('Линейно независимая матрица')




# Task 6
# russian_alphabet = {
#     'а': 'А',
#     'б': 'Б',
#     'в': 'В',
#     'г': 'Г',
#     'д': 'Д',
#     'е': 'Е',
#     'ё': 'Ё',
#     'ж': 'Ж',
#     'з': 'З',
#     'и': 'И',
#     'й': 'Й',
#     'к': 'К',
#     'л': 'Л',
#     'м': 'М',
#     'н': 'Н',
#     'о': 'О',
#     'п': 'П',
#     'р': 'Р',
#     'с': 'С',
#     'т': 'Т',
#     'у': 'У',
#     'ф': 'Ф',
#     'х': 'Х',
#     'ц': 'Ц',
#     'ч': 'Ч',
#     'ш': 'Ш',
#     'щ': 'Щ',
#     'ъ': 'Ъ',
#     'ы': 'Ы',
#     'ь': 'Ь',
#     'э': 'Э',
#     'ю': 'Ю',
#     'я': 'Я'
#     }

# print('Введите количество слов, из которых будет состоять аббревиатура: ')
# amount = int(input())

# print('Введите слова для аббревиатуры через enter: ')
# words = []

# for i in range(0, amount):
#     word = str(input())
#     words.append(word)

# for word in words:
#     print(russian_alphabet.get(word[0]), end='')
