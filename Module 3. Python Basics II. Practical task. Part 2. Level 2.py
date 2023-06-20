from random import randint

n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]

x = []
print('Случайным образом сгенерированная матрица:')
for i in range(len(m)):
    if m[i] == m[0]:
        print('[', m[i], ',', sep='')
    elif m[i] == m[-1]:
        print(' ', m[i], ']', sep='')
    else:
        print(' ', m[i], ',', sep='')
for i in m:
    x.append(sorted(i)[-1])

print(f'Максимальный элемент матрицы: {sorted(x)[-1]}')
