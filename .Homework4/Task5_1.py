#Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

n = int(input("Введите число n: "))
def factorial(n):
    if n != 0:
        return n*factorial(n-1)
    else:
        return 1
def trianular(n):
    if n != 0:
        return n+trianular(n-1)
    else:
        return 0
print(f"{n}! = {factorial(n)}")
print(f"T({n}) = {trianular(n)}")
