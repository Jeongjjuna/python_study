#1. 클래스 기본구조
class Person(object):
    def __init__(self, name):
        self.name = name

    def say_something(self):
        print(f"I am {self.name}. hello")

    def run(self, num):
        print('run'*num)



#2. 생성자 소멸자
class Person(object):
    def __init__(self, name): #생성자
        self.name = name

    def say_something(self):
        print(f"I am {self.name}. hello")

    def run(self, num):
        print('run'*num)

    def __del__(self): #소멸자
        print("good bye")

person = Person('Mike')
del person #소멸자를 이용하여 클래스객체 지우기



#3. 클래스의 계승(상속)
class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')


car = Car()
car.run()
print("##########")
toyota_car = ToyotaCar()
toyota_car.run() #부모의 함수를 사용할 수 있다.
print("##########")
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()


#4. 메소드 오버라이드(재정의 덮어쓰기) 및 super().__init__
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def run(self):
        print('run')


class ToyotaCar(Car):
    def __init__(self, model, color, year):
        super().__init__(model, color) #두개는 이전 것을 사용하겠다
        self.year = year #ToyotaCar에서만 사용하는 생성자 파라미터
    
    def run(self): #오버라이딩
        super().run() #부모 메소드 실행가능
        print('fast')


class TeslaCar(Car):
    def run(self): #오버라이딩
        print('super fast')

a = ToyotaCar(1,2,3)
a.run()