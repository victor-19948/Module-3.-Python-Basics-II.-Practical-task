n = str(input('Введите целое число: '))
x = 0
for i in n:
    x += int(i)
print(f'сумма цифр введенного числа равна: {x}')