#import lesson_package.utils
#풀네임을 쓰는걸 선호하는 회사들이 있음(어디서 왔는지 명확하기 때문에)
#import lesson_package.utils
#r = lesson_package.utils.say_twice('hello')
#print(r)

#최소한 어디 모듈(파일)인지까지는 알려주면 좋다.
from lesson_package import utils
r = utils.say_twice('goot night')
print(r)


from lesson_package.talk import human
print(human.sing())