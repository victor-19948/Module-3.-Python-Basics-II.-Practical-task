a = [56, 9, 11, 2]
b = [3, 81, 5]


def max_number(a):
    c = []
    for i in a:
        j = str(i)
        c.append(int(j[0]))
    c_sorted = tuple(c)
    c_sorted = sorted(c_sorted, reverse=True)
    index = []
    for i in range(len(c_sorted)):
        for j in range(len(c)):
            if c_sorted[i] == c[j]:
                index.append(j)
    a_new = []
    for i in index:
        a_new.append(a[i])
    a_new_str = ''
    for i in a_new:
        a_new_str += str(i)
    return int(a_new_str)
