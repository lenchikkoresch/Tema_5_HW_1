# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

c = int(input("Введите трехзначное число: "))
n=c
summa = 0
while n>0:
    x = n % 10
    summa = summa + x
    n = n // 10
print (f"Сумма цифр числа {c} равна {summa}.")




