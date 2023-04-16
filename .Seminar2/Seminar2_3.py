n = int(input("Введите количество арбузов: "))
max = min = int(input("Введите вес 1-го арбуза в кг: "))
for i in range(2,n+1):
    m1 = int(input(f"Введите вес {i}-го арбуза в кг: "))
    if m1 > max:
        max = m1
    elif m1 < min:
        min = m1
print(f"Абруз для тещи весит {min} кг")
print(f"Абруз для себя любимого весит {max} кг")