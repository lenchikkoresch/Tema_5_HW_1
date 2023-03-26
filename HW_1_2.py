# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

c = int(input('Введите трехзначное число: '))
n=c
summa=0
while n>0:
    x = n % 10
    summa = summa + x
    n = n // 10
print (f"Сумма цифр числа {c} равна {summa}.")


# можно решить через строку
c = input("Введите трехзначное число: ")
if len(c)!=3:
    print ("Вели не трехзначное число")
else:
    summa = int(c[0]) + int(c[1]) + int(c[2])
print (f"Сумма цифр числа {c} равна {summa}.")


c = input("Введите трехзначное число: ")
sum=0
if len(c)!=3:
    print ("Вели не трехзначное число")
else:   
    m = len(c)
    for i in c:
        sum += int(i)
    print (f"Сумма цифр числа {c} равна {sum}.")
    

#Почему не работает этот код
c = input('Введите трехзначное число: ')
if type(c) == int:
    n = int (c)
    summa=0
    while n>0:
        x = n % 10
        summa = summa + x
        n = n // 10
    print (f"Сумма цифр числа {c} равна {summa}.") 
else:
    print ("Ввели не число")  

    
