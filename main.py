a = input("Введите число: ")
n = int(a)
summ = 0
while n>0:
    x = n%10
    summ = summ + x
    n = n/10
print (f"сумма цифр числа {a} равнa {round(summ)}")






