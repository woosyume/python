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
    # Mon apple coffee
    # Tue banana smoothie
    # Wed mango tea

# Dict to for loop ... Dict = tuple with list [(), ()]
d = {'x': 100, 'y': 200}
for v in d.items():
    print(v)

for k, v in d.items():
    print(k, v)

# Define method
def say_something():
    print('Hi')

say_something()
print(type(say_something)) # <class 'function'>

def return_something():
    return 'Hi'

result = return_something()
print(result)

## With parameter
def what_is_this(color):
    print(color)

what_is_this('red')

# 이런 식의 書き方も可能
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num(1, 2)
print(r)

def menu(entree, drink, dessert):
    print(entree, drink, dessert)

menu('beef', 'beer', 'ice')
# 파라미터에 키워드도 지정 가능
menu(entree='beef', drink='beer', dessert='ice')

## Default parameter
def team(name='barcelona', captain='messi'):
    print(name, captain)
team() # barcelona messi
team(name='psg') # psg messi

def test_func(x, l=[]):
    l.append(x)
    return l
# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)

# 그런데 리스트는 디폴트 파라미터로 넘겨선 안된다는 암묵적인 룰이 있다.
r = test_func(100)
print(r) # [100]
r = test_func(100)
print(r) # [100, 100]

# 'l'은 함수 선언할 때 한번만 만들어지고 그 뒤엔 동일한 것을 참조하게 된다. バグに繋がりやすい

def test_func(x, l=None):
    if l is None: # 이런 식으로 None으로 설정해둔 후에 都度都度初期化
        l = []
    l.append(x)
    return l
r = test_func(100)
print(r) # [100]
r = test_func(100)
print(r) # [100]

# Make tuple with parameter (*args)
def say_something(*args):
    for arg in args:
        print(arg)
say_something('hi', 'woosyume')

def say_something(particular, *args):
    print(particular)
    for arg in args:
        print(arg)
say_something('Hi', 'Woosyume', 'Hoho') # 위치를 알아서 찾아가나보다. line143에 비해 많이 사용된다.
t = ('Woosyume', 'Rakuten')
say_something('Wow!', *t)

# Make dict with keyword parameter (**kwargs)
def menu(**kwargs):
    # print(entree, drink)
    for k, v in kwargs.items():
        print(k, v)
menu(entree='burger', drink='coke')

d = {
    'entree': 'beef',
    'drink': 'coffee'
}
menu(**d) # 이 형태 많이 쓰인다.

def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana', 'apple', 'orange', entree='beef', drink='coke')
# banana
# ('apple', 'orange')
# {'entree': 'beef', 'drink': 'coke'}