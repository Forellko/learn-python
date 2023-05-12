def func(a,b,c):
    return a + b + c

arr = {'a': 1, 'b': 2, 'c': 3}

result = func(**arr)

print(result)