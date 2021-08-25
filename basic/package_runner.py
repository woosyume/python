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