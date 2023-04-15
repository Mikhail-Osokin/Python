n = int(input("Введите количество монеток: "))
reshka = 0
orel = 0
for i in range(n):
    m = input(f"Введите для {i}-ой монетки 'орел' или 'решка': ")
    if m == "орел":
        orel += 1 
    else:
        reshka +=1
if orel > reshka:
    print(f"Необходимо перевернуть {reshka} раз")
else:
    print(f"Необходимо перевернуть {orel} раз")