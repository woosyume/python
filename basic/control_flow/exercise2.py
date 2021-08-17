count = 0
while count <= 5:
    print(count)
    count += 1
else: # finally같은 느낌으로 실행되는구나. break로 빠져나가지 않는 한 실행된다.
    print('done')

# continue, break 도 마찬가지로 존재한다.

# Input method
# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('next')

# For loop
some_list = [1, 2, 3, 4, 5]

for i in some_list:
    print(i)

for s in 'abcde':
    print(s)
# a
# b
# c
# d
# e

for word in ['My', 'name', 'is', 'woosyume']:
    print(word)

for fruit in ['apple', 'banana', 'orange']:
    print(fruit)
else:
    print('done')

# Range method
# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(-1, 10, 2): # range(10), range(2, 10, 3) 와 같은 형태도 출력 가능
    print(i)

## i를 사용하지 않는 경우 _ 로 한다. 인덱스를 사용하지 않는다는 것을 의미
for _ in range(10):
    print('hello')

# Enumerate method
for i, fruit in enumerate(['apple', 'banana']):
    print(i, fruit)

# Zip method
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'mango']
drinks = ['coffee', 'smoothie', 'tea']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)