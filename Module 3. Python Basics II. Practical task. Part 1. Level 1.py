x = int(input('Введите значение вклада в банке: '))
p = float(input('Введите процент ежегодного увеличения вклада: '))
y = int(input('Введите конечное значение вклада в банке: '))
years = 0
word = 'лет'
while 1:
    if x < y:
        x = x + int(x * (p * 0.01))
        years += 1
    else:
        if years == 1:
            word = 'год'
        elif 1 < years < 5:
            word = 'года'
        print(f'вклад в банке составит не менее {y} рублей через {years} {word}')
        break
