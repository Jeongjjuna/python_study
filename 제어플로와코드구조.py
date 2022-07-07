#1. 주석
'''변수 설명을 변수 위에 써주도록 하는것이 암묵적 룰이다'''
#Apple price
some_value = 100 


#2. 한줄이 길어서 줄바꿈 하고싶을 때
'''백슬래쉬, 소괄호를 통해 줄바꿈해서 출력 가능'''
x = 1 + 1 + 1 + 1 + 1 +\
    1 + 1 + 1 + 1 + 1

y = (1 + 1 + 1 + 1 + 1 +
    1 + 1 + 1 + 1 + 1)


#3. if문

#4. 디버거사용

#5. 논리연산자

#6. in 과 not
'''수치에 not은 잘 사용하지 않고 !를사용. boolen형에 not을 사용'''
is_ok = True
if not is_ok:
    print('ok')

a, b = 1, 2
if a != b:
    print("diff")


#7. 값이 들어있지 않다고 판정
'''False = 0, 0.0, '', [], (), {}, set()'''


#8. None판정(아무것도 없는 상태(객체))
''' 
is는 주로 변수가 None객체인지 아닌지 판별할 때 사용한다.
수치 비교는 ==등호를 사용한다.
'''
is_empty = None
if is_empty is None:
    print("None!!")


#9. while, continue, break

#10. while else문
''' while문에 @@break가 걸리지 않고 빠져나왔을 때@@ else문 한번 실행시키고 종료'''
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("done")\


#11. input

#12. for, break, continue

#13. for else문
'''while else문과 같이 break가 걸리지 않고 모든 반복이 끝났을때 else문 까지 실행하고 종료한다.'''


#14. ragne함수

#15. enumerate함수

#16. zip함수

#17. 사전을 for문으로 처리
d = {'x': 100, 'y': 200}
print(d.items())
for k, v in d.items():
    print(k, ':', v)

#18. 함수정의

#19. 함수 인자와 반환값의 선언
'''단순 보기좋은 표기뿐이란 것을 상기하자!'''
def add_num(a: int, b: int) -> int:
    return a + b

#20. 위치 인수, 키워드 인수, 디폴트 인수
'''정확히 명시해주면 순서가 바껴도 상관없다'''
def menu(entree, drink, dessert):
    print('test')

menu(entree="beef", dessert='ice', drink='beer')


#21. 디폴트 인수를 쓸 때 주의할 점
'''파이썬에서 [], {}의 빈 자료형들은 디폴트 값으로 사용하면 에러발생확률이 높아 사용하지 않음'''
def test_func(x, l=[]): #잘못된 예시
    l.append(x)
    return l

def test_func(x, l=None): #올바른 예시
    if l is None:
        l = []
    l.append(x)
    return l


#22. 위치 인수의 튜플화
'''여러개 인수를 튜플형태로 받는다.
*args에 튜플형태로 넣어줘도 된다.'''
def say_something(*args):
    for arg in args:
        print(arg)

say_something('Hi', 'Mike', 'Nance')

def say_something(word, *args):
    for arg in args:
        print(arg)

say_something('Hi', 'Mike', 'Nance')


#23. 키워드 인수의 사전화
def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)
menu(entree='beef', drink='coffee')

d = {
    'entree':'beef',
    'drink':'ice coffee',
    'dessert':'ice'
}
menu(**d)
'''d의 딕셔너리가 그대로 kwargs에 딕셔너리 형태로 넘어간다'''

