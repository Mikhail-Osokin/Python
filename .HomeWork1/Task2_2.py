n = int(input("Введите верхнюю границу двух чисел: "))
for i in range(n):
    for j in range(n):
        if i*j == i+j:
            print(f"Чило {i} и число {j} удовлетворяют условию")