n = int(input("Введите целое неотрицательное число: "))
i = 1
f = 1
while i <= n:
    f = i*f
    i += 1
print(f"{n}! = {f}")