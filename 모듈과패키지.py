#1. 커맨드 라인 인수
''' 
명령어 : $ C:/Jihun/anaconda3/python.exe 모듈과패키지.py option1 option2 option3 
실행결과 : ['모듈과패키지.py', 'option1', 'option2', 'option3']
            모듈과패키지.py
            option1
            option2
            option3
'''
import sys
print(sys.argv)

for i in sys.argv:
    print(i)