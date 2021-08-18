# 타 언어와 다르게 메소드 내부에 코멘트 기입
def example_func(param1, param2):
    """Example description
    
    Args:
        param1 (int): ...
        param2 (str): ...

    Returns:
        bool: ...
    """
    print(param1)
    print(param2)
    return True

# print(example_func.__doc__)
# help(example_func)

# Function in Function ... 해당 함수 내에서만 사용되는 함수가 있을 때 정의. private의 더 좁은 형태라고 생각할 수 있겠다.
def outer(a, b):
    def plus(c, d):
        return c + d
    print(a, b)

    r = plus(a, b)
    print(r)

outer(1, 2)

# Closure
def outer(a, b):
    def inner():
        return a + b
    return inner # 함수를 그대로 리턴

f = outer(1, 2)
r = f()
print(r)

## another example : 나중에 쓰고싶을 때 용도에 따라 사용여부를 나눌 수 있다
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius # 実行せずにまずReturn
    return circle_area

cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)

# print(cal1()) # TypeError: circle_area() missing 1 required positional argument: 'radius'
print(cal1(10)) # 314.0
print(cal2(10)) # 314.1592

# Decorator : 함수의 전후에 무언가 추가적인 전/후 처리를 하고 싶을 때
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs) # 이 샘플에서는 add_num이 들어가 있다
        print('end')
        return result
    return wrapper

## Decorator 사용 중이라는 의미 ... @method_name
@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

# Lambda
l = ['Mon', 'tue', 'Wed', 'Thu', 'sat', 'Sun']
def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     # 맨 앞자리를 대문자로 바꿔서 리턴
#     return word.capitalize()

# 이렇게 쓰는 것이 람다
sample_func = lambda word: word.capitalize()

change_words(l, sample_func)
# Mon
# Tue
# Wed
# Thu
# Sat
# Sun

# Generator : 반복처리 + 정제
l = ['Good morning', 'Good afternoon', 'Good night']
for i in l:
    print(i)

## With generator...제네레이터를 기억하고 있기 때문에 next를 통해 다음으로 넘어간다. 각 출력 상태를 기억

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

for g in greeting():
    print(g)

g = greeting()
print(next(g))
print('@@@@')
print(next(g))
print('@@@@')
print(next(g))
# Good morning
# @@@@
# Good afternoon
# @@@@
# Good night

def counter(num=10):
    for _ in range(num):
        yield 'run'

generator = counter()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator)) # StopIteration