from operator import itemgetter

params = {'a': 1, 'b': 2}

a, b = itemgetter('a', 'b')(params)

print(a, b)