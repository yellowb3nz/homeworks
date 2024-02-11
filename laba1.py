##Задание 1
# var1 = int(input('Введите первое число: '))
# var2 = int(input('Введите второе число: '))
# var3 = int(input('Введите третье число: '))

# if var1 == var2 == var3:
#     print("Количество совпадений: 3")
# elif var1 == var2 or var1 == var3 or var2 == var3:
#     print("Количество совпадений: 2")
# else:
#     print("Количество совпадений: 0")

##Задание 2.1
# amount = int(input("Введите натуральное число n: ")) + 1
# line = ""
# for i in range(1, amount):
#     k = str(i)
#     line += k
#     print(line)

#Задание 2.2
n = int(input("Введите натуральное число n: "))
for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end="")
        
    for j in range(i, 1, -1):
        print(j, end="")
        
    for j in range(1, i+1):
        print(j, end="")
        
    print()


    
    
    
    

