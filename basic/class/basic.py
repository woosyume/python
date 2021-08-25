# class Person: 이것도 파이썬3 부터는 가능하지만 2와의 호환성, 상속 등을 위해 안쓰는게 암묵적 룰
class Person(object):
    # Seems like constructor
    # self를 통해 자기 자신에게 값을 저장
    def __init__(self, name) -> None:
        self.name = name
        print(self.name)
        
    def say_something(self):
        print('I am {}. Hello'.format(self.name))
        self.run()

    def run(self):
        print('run')

    # Object가 더 이상 사용되지 않을 때 실행됨. Deconstructor
    def __del__(self):
        print('good bye')
person = Person('Woosyume')
person.say_something()

# Extension
class Person(object):
    def __init__(self, age=1) -> None:
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('Drive ok')
        else:
            raise Exception('No Driver License')

class Baby(Person):
    def __init__(self, age=1) -> None:
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age=18) -> None:
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()

car = Car()
# car.ride(baby)
car.ride(adult)


class ToyotaCar(Car):
    def run(self):
        print('toyota run')
    # pass

class TeslaCar(Car):
    def __init__(self, model,
     enable_auto_run=False,
      password='123'):
        # 같은 부분에 대해서는 부모 생성자 호출
        super().__init__(model=model)
        self.__enable_auto_run = enable_auto_run
        self.password = password
        print('hmm...', self.password)

    # 읽기는 가능한데 쓰기는 불가능하도록 하는 것이 프로퍼티
    @property
    def enable_auto_run(self):
        return self.__enable_auto_run

    # property를 쓰기 가능하도록 할 때는 이것을 활용
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.password == '456':
            self.__enable_auto_run = is_enable
        else:
            raise ValueError

    def auto_run(self):
        print('aaa:', self.__enable_auto_run)
        print('auto run')

car = Car()
car.run()
print('###########')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('###########')
tesla_car = TeslaCar('Model S', password='456')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)

# print(tesla_car.enable_auto_run)
# 이것을 금지하고 싶을 때 enable_auto_run -> _enable_auto_run or ___enable_auto_run
# _ : "볼 수는 있지만 건드리지는 말았으면 좋겠어."
# __ : "아예 못 보게 할거야. 건드릴 생각 마."
# __enable_auto_run 인 경우에는 클래스 내부에서만 접근 가능.
# tesla_car.enable_auto_run = True ... AttributeError: can't set attribute
# print(tesla_car.enable_auto_run)

class T(object):
    pass

# 이런 식으로 값을 세팅하는 일은 거의 없다고 한다.
t = T()
t.name = 'woosyume'
t.age = 20
print(t.name)