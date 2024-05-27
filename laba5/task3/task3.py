with open("C:\\Users\\Danya\\Desktop\\laba5\\task3\\children.txt", 'r') as file:
    lines = file.readlines()

max_age = 0
min_age = float('inf')
oldest_child = ""
youngest_child = ""

for line in lines:
    surname, name, age = line.split()
    age = int(age)
    
    if age > max_age:
        max_age = age
        oldest_child = f"{surname} {name} {age}"
    
    if age < min_age:
        min_age = age
        youngest_child = f"{surname} {name} {age}"

with open("C:\\Users\\Danya\\Desktop\\laba5\\task3\\oldest.txt", 'w') as file:
    file.write(oldest_child)

with open("C:\\Users\\Danya\\Desktop\\laba5\\task3\\youngest.txt", 'w') as file:
    file.write(youngest_child)