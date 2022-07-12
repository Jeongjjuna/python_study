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


#5. Property를 사용한 속성의 설정(속성을 마음대로 바꾸기 싫을 때)
#-------------------------------밖에서 속성을 쉽게 바꿀 수 있음---------------------
class Car:
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

    def run(self):
        print('super fast')


TeslaCar = TeslaCar('Model S')
TeslaCar.enable_auto_run = True
print(TeslaCar.enable_auto_run)

#-------------------------------밖에서 속성값을 쉽게 바꿀 수 없도록 하고 싶을 때------

class Car:
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class TeslaCar(Car):
    def __init__(self, model='Model S',
                        enable_auto_run=False,
                        passwd='123'):
        super().__init__(model)
        #언더스코어(_)1개는 명시적으로 외부에서 속성값을 바꾸지 않았으면 좋겠다 라는 뜻이다
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property #기본적으로 못바꾸게 한다
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter #passwd값을 잘못읽으면 에러발생시키고 잘 입력시키면 True로 바꿔준다
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('super fast')


TeslaCar = TeslaCar('Model S', passwd='123')
#TeslaCar.enable_auto_run = True #수정할 수 없다는 에러(ok)
TeslaCar.enable_auto_run = True
print(TeslaCar.enable_auto_run)

#------------------ 언더스코어2개(__)에 관한 것은 다음에 공부---------------------