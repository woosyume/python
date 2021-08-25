class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')

class Car(object):
    def run(self):
        print('run')

# 메소드가 오버라이드 되어있는 경우, 먼저 상속된 부분이 우선 호출
## 다만 복잡성이 늘기 때문에 꼭 필요한 것이 아니면 쓰지 않는 것이 좋다.
class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()