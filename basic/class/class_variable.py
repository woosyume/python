class Person(object):
    # 모든 오브젝트에서 공유된다. 사용에 주의할 것
    kind = 'human'
    
    def __init__(self, name) -> None:
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

# 리스트같은 것은 누적되기 때문에 아래와 같은 사용에는 주의. 
class T(object):
    words = []

    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add 1')
c.add_word('add 2')
print(c.words)

d = T()
d.add_word('add 3')
d.add_word('add 4')
# ['add 1', 'add 2', 'add 3', 'add 4']
print(d.words)