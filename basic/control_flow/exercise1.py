# Comment out
"""
test
test
test
"""
# 파이썬에서는 변수에 대한 코멘트를 옆이 아닌, 이처럼 위에 쓰는 것이 암묵적인 룰
some_value = 100

# 한 줄이 길어질 때 백슬래시('\') 사용
s = 'aaaaaaaa' \
 + 'bbbbbbbb'
print(s)

## 백슬래시가 싫다면 괄호도 가능
s = ('aaaaaaaa' 
 + 'bbbbbbbb')
print(s)

 # If
x = -10
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

a = 5
b = 10
if a > 0:
    print('a is positive')
    if b > 0: 
        print('b is positive')

# In and Not
y = [1, 2, 3]
x = 1
if x in y:
    print('Yes')

if x not in y:
    print('Yes')

# 값이 들어 있지 않은 판정을 할 때
is_okay = True
# 굳이 is_okay == True 이렇게 안한다.
if is_okay: 
    print('Hello')

if not is_okay:
    print('이런 not의 書き方는 괜찮다.')

## 값이 들어있는지 아닌지 확인할 때.
## is_blank = [] 이런 것도 확인 가능 
is_blank = ''
if is_blank:
    print('OK!')
else:
    print('NO!')

# None Object의 판정
is_empty = None
# if is_empty None: ... 이거는 안된다!!
# is not 도 가능
if is_empty is None:
    print('Not exist!')

## is란?
print(1 == True) # True 
print(1 is True) # False ... 완전히 동일 오브젝트인지 확인하는 것이 is
## None 판정할때 가장 많이 쓰이는 것이 is