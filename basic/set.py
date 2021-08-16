# Set ... not allow duplication
a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a) # {1, 2, 3, 4, 5, 6}

b = {1, 2, 3, 7}
print(a - b) # {4, 5, 6}
print(b - a) # {7}
print(a | b) # {1, 2, 3, 4, 5, 6, 7}
print(a ^ b) # {4, 5, 6, 7}
print(a & b) # {1, 2, 3}

# Methods
s = {1, 2, 3, 4, 5}
# 리스트와 다르게 인덱스가 없다.
s.add(6)
print(s) # {1, 2, 3, 4, 5, 6}

s.remove(6)
print(s) # {1, 2, 3, 4, 5}

s.discard(3)
print(s) # # {1, 2, 4, 5}

# print(help(set))

# Sample : 공통점 찾기 등
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends) # {'D'}

## Another sample : 장바구니
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f) # change list to set avoiding duplicated values
print(kind)