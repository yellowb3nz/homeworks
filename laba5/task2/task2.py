with open("C:\\Users\\Danya\\Desktop\\laba5\\task2\\numbers.txt", 'r') as file:
    numbers = [int(number) for number in file.readlines()]

result = [i for i in numbers]
result.sort()

with open("C:\\Users\\Danya\\Desktop\\laba5\\task2\\output.txt", 'w') as file:
    file.writelines("%s\n" % i for i in result)