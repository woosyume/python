import math # 파이썬은 대부분의 수학 함수가 마련되어 있다.
print(help(math))

num = 1
# num: int = 1 와 같이 형태 지정도 가능. 그런데 딱히 필요하지는 않다.
name = 'Kim'
is_os = True

print(num, type(num))
print(name, type(name))
print(is_os, type(is_os))

test_num = '1'
print(test_num)

print('Hi', 'woosyume', sep=',', end='.\n') # Hi,woosyume.

print(17 / 3) # 5.666666666666667
print(17 // 3) # 5
print(17 % 3) # 2
print(5 ** 2) # 25

print(round(3.141592, 2)) # 3.14