# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических 
# операций допускаются только +1 и -1. Также нельзя использовать циклы.

a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
def sum(a, b):
    if b != 0:
        return 1+sum(a, b-1)
    else:
        return a
print(f"{a} + {b} = {sum(a,b)}")
