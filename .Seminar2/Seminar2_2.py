n = int(input("Введите число: "))
i = 0
j = 1
count = 1
while j < n:
    # j = j + i
    # i = j - i
    i, j = j, i + j
    count += 1
if j == n:
    print (f"Число {n} является {count}-м числом Фибоначчи, предыдущая итерация которого = {i}")
else:
    print(f"Число {n} не является числом Фибоначчи")