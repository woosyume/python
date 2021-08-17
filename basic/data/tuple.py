# Tuple (読み込み専用で使うことが多い) 추가 및 변환이 불가. 다만 튜플끼리 결합은 가능
t = (1, 2, 3, 4, 1, 2) # == t = 1, 2, 3, 4, 5 ... 컴마를 사용한 시점에서 Tuple扱い
# t = (1) ... 이것은 단순히 int 타입. 컴마가 반드시 필요하다.
# t = (1,) 이런 식으로 컴마를 포함해서 선언해야.
print(t)

# t[0] = 100 # Error
print(t[-1]) # 2
print(t.index(1)) # 1은 어디 인덱스에 있는가?
print(t.index(1, 1))

print(t.count(1)) # 1은 몇 개 있는가?

# 리스트 포함하는 것이 가능
t = ([1, 2, 3], [4, 5, 6])
print(t[0][0])
t[0][0] = 100 # 이것은 되네..
print(t[0][0])

new_tuple = (1, 2, 3) + (4, 5, 6)
print(new_tuple) # (1, 2, 3, 4, 5, 6)

# Unpacking
num_tuple = (10, 20)
print(num_tuple)
x, y = num_tuple
print(x, y) # 10 20

min, max = 0, 100 # 파이썬 구조적으로 이것은 사실 Tuple로 한 번 변환.
print(min, max)

i = 10
j = 20
# tmp = i
# i = j
# j = tmp
i, j = j, i # Simple 치환
print(i, j)

# Sample : '3개 중 2개를 고르시오'와 같은 프로그램
# 後で間違って書き換えないようにすることが主な目的
chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)