n = int(input("Введите количество кустов: "))
a = list()
count = list()
for i in range(n):
    x = int(input(f"Введите количество ягод на {i}ом кусте: "))
    a.append(x)
for i in range(len(a)):
    count.append(a[i-2]+a[i-2]+a[i])
print(f"максимальное количество ягод с 3х соседних кустов = {max(count)}")