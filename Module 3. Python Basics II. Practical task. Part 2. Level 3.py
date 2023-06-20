d = {'name1': 'id1',
     'name2': 'id2',
     'name3': 'id3'}
l1 = list(d.keys())
l2 = list(d.values())
d_new = dict(zip(l2, l1))
print(d)
print(d_new)
