# List
l = [1, 20, 4, 50]
print(l) # [1, 20, 4, 50]

print(l[-1]) # 50... last
print(l[2:]) # [4, 50]
print(len(l))
print(list('abcde')) # ['a', 'b', 'c', 'd', 'e']

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(n[::2]) # [1, 3, 5, 7, 9]
print(n[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Nested list
a = ['a', 'b']
n = [1, 2, 3]
x = [a, n]
print(x) # [['a', 'b'], [1, 2, 3]]
print(x[0][1]) # b
print(x[1][2]) # 3

s = ['a', 'b', 'c', 'd', 'e']

# 문자열은 안되지만 배열에서는 書き換えが可能
s[0] = 'X'
print(s) # ['X', 'b', 'c', 'd', 'e']

s[3:5] = [1, 2, 3]
print(s) # ['X', 'b', 'c', 1, 2, 3]

s[1:2] = []
print(s) # ['X', 'c', 'd', 'e']

s[:] = []
print(s) # []

###

n = [1, 2, 3, 4, 5]
n.append(100)
print(n) # [1, 2, 3, 4, 5, 100]

n.insert(0, 0)
print(n) # [0, 1, 2, 3, 4, 5, 100]

print(n.pop()) # 100
print(n.pop(1)) # 1

del n[0]
print(n) # [2, 3, 4, 5]

n.remove(4)
print(n) # [2, 3, 5]

# n.remove(999) # ValueError: list.remove(x): x not in list

# del n
# print(n) # NameError: name 'n' is not defined

# Merge lists
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # [1, 2, 3, 4, 5, 6]
# c = b.extend(a) ... extend는 in-place 함수라 a를 직접 변경한다.
a.extend(b) # [1, 2, 3, 4, 5, 6]
print(a)

# Methods of list
r = [1, 2, 3, 4, 5, 6 , 7, 3]
print(r.index(5)) # 4 ... 해당 값의 인덱스 구하는 함수
print(r.index(3, 3)) # 7 ... 두 번째 값도 확인
print(r.count(3)) # 2 ... 개수

if 99 in r:
    print('exist')
else:
    print('not exist')

r.sort()
print(r) # [1, 2, 3, 3, 4, 5, 6, 7]
r.sort(reverse=True)
print(r) # [7, 6, 5, 4, 3, 3, 2, 1]
r.reverse()
print(r) # [1, 2, 3, 3, 4, 5, 6, 7]

s = 'My name is woosyume'
to_split = s.split(' ')
print(to_split) # ['My', 'name', 'is', 'woosyume']

x = ' '.join(to_split)
print(x) # My name is woosyume

# List Copy
i = [1, 2, 3, 4 ,5]
j = i # 이런 Copy는 주의해야 한다.
j[0] = 100 # i를 참조하고 있기 때문에 같이 바뀌어버린다.
print('i=', i)
print('j=', j)
# i= [100, 2, 3, 4, 5]
# j= [100, 2, 3, 4, 5]

x = [1, 2, 3, 4, 5]
y = x.copy() # Copy를 하면 별도 참조 생성 ... y = x[:]도 같은 역할.
y[0] = 100
print('x=', x)
print('y=', y)
# x= [1, 2, 3, 4, 5]
# y= [100, 2, 3, 4, 5]

X = 20
Y = X
print(id(X)) 
print(id(Y)) # Same hash with the above
Y = 5
print(id(X)) 
print(id(Y)) # Different hash with the above

# Sample
seat = []
min = 0
max = 9
min <= len(seat) < max
# True