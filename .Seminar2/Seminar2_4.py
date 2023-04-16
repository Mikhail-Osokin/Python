n = int(input("Введите количество наблюдаемых дней: "))
max = 0
count = 0
for i in range(1, n+1):
    m1 = int(input(f"Введите температуру в {i} день: "))
    if m1 > 0:
        count +=1
    else:
        if count > max:
            max = count
        count = 0
if count > max:
    max = count
print(f"Максимальное количество дней с плюсовой температурой = {max}")