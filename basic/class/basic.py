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
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('toyota run')
    # pass

class TeslaCar(Car):
    def __init__(self, model, enable_auto_run=False):
        # 같은 부분에 대해서는 부모 생성자 호출
        super().__init__(model=model)
        self.enable_auto_run = enable_auto_run

    def auto_run(self):
        print('auto run')

car = Car()
car.run()
print('###########')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('###########')
tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()