s = 'test'
print(s)

print('Hi! \n Woosyume')
print(r'C:\name\name') # r is 'raw'

print("#############")
print("""\
line1
line2
line3\
""")
print("#############")

# \n 과 같지만 가독성을 위해 더블 쿼테이션 이용 가능
# line1
# line2
# line3

print('Hi. ' * 3 + 'Woosyume') # Hi. Hi. Hi. Woosyume

prefix = 'Py'
print(prefix + 'thon')

text = ('aaaaaa'
        'bbbbbbb')
print(text) # aaaaaabbbbbbb

word = 'Python'
print(word[0]) # P
print(word[-1]) # n ... the last index
print(word[0:2]) # Py
print(word[:2]) # Py
print(word[2:]) # thon

# word[0] = 'j' # 이렇게 바로 대입은 불가
word = 'j' + word[1:]
print(word)

n = len(word)
print(n)

################ String Methods ################
s = 'My name is woosyume. Hi woosyume.'
print(s)
is_start = s.startswith('A')
print(is_start) # False

print(s.find('woosyume')) # 11
print(s.rfind('woosyume')) # 2 .. 거꾸로 찾기
print(s.count('woosyume')) # 2
print(s.capitalize()) # My name is woosyume. hi woosyume.
print(s.title()) # My Name Is Woosyume. Hi Woosyume.

print('a is {}, {}, {}'.format('woosyume', 'A', 'B')) # a is woosyume, A, B
# 인덱스 직접 지정도 가능
print('My name is {0} {1}'.format('Woohyeok', 'Kim')) # My name is Woohyeok Kim
print('My name is {last} {first}'.format(last='Woohyeok', first='Kim')) # My name is Woohyeok Kim

# Python 3.6~ f-strings함수가 사용 가능
last = 'Woohyeok'
first = 'Kim'
print(f'My name is {last} {first}') # My name is Woohyeok Kim