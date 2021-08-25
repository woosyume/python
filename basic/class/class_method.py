class Person(object):

    kind = 'human'

    def __init__(self) -> None:
        self.x = 100

    # 오브젝트로서 생성하지 않아도 접근 가능하도록 하는 경우 @classmethod를 사용
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about():
        print('about human')

a = Person()
print(a.x)
# 아직 오브젝트화 되지 않은 것.
b = Person
# # 와 이건 출력되는구나.
# print(b().x)
print(b.what_is_your_kind()) # human
print(Person.what_is_your_kind()) # human

######## Static Method : 쓸 일은 많지 않다
Person.about()
