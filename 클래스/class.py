#1. 클래스 기본구조
class Person(object):
    def __init__(self, name):
        self.name = name

    def say_something(self):
        print(f"I am {self.name}. hello")

    def run(self, num):
        print('run'*num)