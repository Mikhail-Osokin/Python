# Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
# -> 9
def abs(x):
    if x < 0:
        x = x*(-1)
    return (x)
n = int(input("Введите количество элементов одномерного массива: "))
a = [0]*n
count = 0
for i in range(n):
    a[i] = int(input(f"Введите {i}-й элемент одномерного массива: "))
x = int(input("Введите искомое число: "))
for i in range(n):
    if 0 <= abs(x-a[i]) <= 1:
        count += 1
        print(f"{count}-е вхождение числа самого близкого искомому {x} в одномерном массиве находится на {i}-й позиции и равно {a[i]}")

