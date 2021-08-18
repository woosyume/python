# 리스트 내포표기
t = (1, 2, 3, 4, 5)
r = []
for i in t:
    r.append(i)

# 이렇게 하면 라인 3~5와 같다. append 함수를 호출하기 때문에 더 빠르다.
r = [i for i in t if i % 2 == 0]
print(r)

t2 = (5, 6, 7, 8, 9, 10)
r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)

r = [i * j for i in t for j in t2]
# Result is same with line 16
print(r)

## 그렇지만 너무 길어져서 코드가 읽기 어려워진다 싶으면 그냥 일반적인 appendの書き方 하는 것이 낫다.

# Dictionary 내포표기
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']
d = {}

for x, y in zip(w, f):
    d[x] = y

print(d) # {'mon': 'coffee', 'tue': 'milk', 'wed': 'water'}

d = {x: y for x, y in zip(w, f)}
print(d) # {'mon': 'coffee', 'tue': 'milk', 'wed': 'water'}

# Set의 내포표기 (Similar with list)
s = set()

for i in range(10):
    s.add(i)

print(s)

s = {i for i in range(10)}
print(s)

# Generator 내포표기
def g():
    for i in range(10):
        yield i

g = g()
print(type(g)) # <class 'generator'>

print(next(g))
print(next(g))
print(next(g))

g = (i for i in range(10))
# g = tuple(i for i in range(10)) 이렇게 하면 튜플이 된다..

print(g)

# Namespace and scope
animal = 'cat'
def f():
    # print(animal) # "animal" is not defined

    animal = 'dog'
    print('local:', locals())

print('global:', globals())

def doc():
    """
    Test Test Doc
    """
    print('name:', doc.__name__)
    print('doc:', doc.__doc__)

doc()

# Error Handling
l = [1, 2, 3]
i = 5
try:
    l[i]
except:
    print("Don't worry")

try:
    l[i]
except IndexError as ex:
    # Don't worry list index out of range
    print("Don't worry: {}".format(ex))
except Exception as ex:
    print('any errors')
finally:
    # 심지어 except: 를 정의하지 않아도 반드시 실행된다.
    print('run definitely')

try:
    l[i]
except IndexError as ex:
    print(ex)
else:
    # 익셉션 발생없이 로직이 실행된 경우에는 else로 들어간다.
    print('done successfully')

# Initialize Custom Exception
# raise IndexError('test error message')
# l[i] # IndexError: test error message

class TestError(Exception):
    pass

def check():
    words = ['apple', 'orange', 'banana']
    # words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
                raise TestError(word)
               # __main__.TestError: APPLE

check()