# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a = input("Введите число: ")
n = int(a)
summ = 0
while n>0:
    x = n%10
    summ = summ + x
    n = n//10
print (f"сумма цифр числа {a} равнa {summ}")