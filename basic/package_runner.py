# import package.utils # full path..　이것을 선호하는 곳도 있지만 코드 양이 많아진다.
from package.tools import utils # 이게 가장 선호되는 표기법 ... as는 별로 쓰이지 않는다.
# from package.utils import say_twice # 함수가 어디서 불린지 모르기 때문에 선호되지 않음.

# import * 이런것도 가능하지만 피하는 편이 좋음.
from package.talk import human
from package.talk import animal

r = utils.say_twice('Hello')
# Hello!Hello!
print(r)

# sing
print(human.sing())
print(animal.cry())

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

for key in ranking:
    print(key)

# ['A', 'C', 'B']
print(sorted(ranking, key=ranking.get, reverse=True))

# 표준 라이브러리는 임포트를 해주어야 한다. 빌트인 함수는 임포트 없이 사용 가능 (e.g. print())
s = "woosyume"
from collections import defaultdict
d = defaultdict(int)

for c in s:
    d[c] += 1

# defaultdict(<class 'int'>, {'w': 1, 'o': 2, 's': 1, 'y': 1, 'u': 1, 'm': 1, 'e': 1})
# 몇 개 있는지 확인
print(d)
print(d['o'])

# 이렇게 가능하지만 선호되지 않는다. 알파벳 순으로 쓰는 것이 룰.
# import collections, sys
import collections
import os
import sys
# Leave a space
# import 3rd party
print(os.__file__)
# print(sys.path)

# config= package.config ... 임포트 되는 시점에서 바로 실행된다.
import package.talk.animal
print('runner=', __name__)

## 그래서 이런 식으로 안전하게 읽을 수 있도록 한다.
def main():
    package.talk.animal.sing()
    
if __name__ == '__main__':
    main()
    print(__name__)
