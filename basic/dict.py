# Dictionary (like KVS)
d = {'x': 10, 'y': 20}
print(d['x'])

d['z'] = 200
print(d['z']) # 200

d[1] = 999
print(d[1]) # 999

d = {'x': 10, 'y': 20}
print(d.keys()) # dict_keys(['x', 'y'])
print(d.values()) # dict_values([10, 20])

d2 = {'x': 1000, 'y': 500, 'z': 20}
d.update(d2)
print(d) # {'x': 1000, 'y': 500, 'z': 20}

print(d.get('x')) # 1000
print(d.get('zzz')) # None

d.pop('x')
print(d) # {'y': 500, 'z': 20}

del d['y']
print(d) # {'z': 20}

d.clear()
print(d) # {}

print('a' in d) # False

# Copy
x = {'a': 1}
y = x
# 리스트와 마찬가지로 参照渡しになってしまう

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)
# {'a': 1}
# {'a': 1000}

# Sample
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

print(fruits['apple'])