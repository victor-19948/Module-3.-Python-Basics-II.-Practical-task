l = [1, 4, 1, 6, 1, 1, 1, 1, 'hello', 'a', 5, 'hello']
print(f'Произвольный список:\n{l}')
l_new = []
adding = True
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == l[j]:
            adding = True
            for k in l_new:
                if k == l[i]:
                    adding = False
            if adding:
                l_new.append(l[i])

print(f'Повторяющиеся в нем элементы:\n{l_new}')
