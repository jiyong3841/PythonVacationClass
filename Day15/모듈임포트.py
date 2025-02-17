'''
1. import 파일명(모듈) : hello.변수명 또는 함수
2. from 파일명(모듈) import 변수, 함수 또는 클래스 : 함수() 호출 가능
3. from 파일명(모듈) * : 함수()
교재 345 ~ 356 : 내장모듈
'''


# import hello
# from Day15.hello import my_name
#
# hello.self_pr()
# print(hello.water)
#
# hello.my_name("짱구")

# from hello import self_pr
# self_pr()
# my_name("철수")

from hello import*
self_pr()
my_name("맹구")
print(water)