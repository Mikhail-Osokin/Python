# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

n = int(input("Введите число n: "))
def Fib(n):
    if n > 1:
        return Fib(n-1)+Fib(n-2)
    elif n == 1:
        return 1
    else:
        return 0
print(f"Fibonachi({n}) = {Fib(n)}")
