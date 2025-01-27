'''
if 조건식 :
    실행할 코드
'''

a = 7
b = 3
if a > b :
    print("1번 조건문 : a가 b보다 큽니다")

if a < b:
    print("2번 조건문 : a가 b보다 큽니다")

age = 20
if age >= 20:
    print("성인입니다.")

number = 10
if number < 10:
    print("10 미만")
if number == 10:
    print("똑같다!")
if number > 10:
    print("10보다 커요")

'''
if 조건식 : 
    조건식이 참일때
else : 
    조건식이 거짓일때 
'''

fruit = "바나나"
if fruit == "바나나" :
    print("저는 바나나를 좋아해요")
else:
    print("바나나 그닥")

num = -3
if num >= 0:
    print("양수입니다.")
else:
    print("음수입니다.")

gender = "man"
if gender == "man":
    print("남자입니다.")
else:
    print("여자입니다.")

number = int(input("숫자를 입력해주세요 : "))
if number % 7 == 0:
    print(f"{number}는 7의 배수입니다.")
else:
    print(f"{number}는 7의 배수가 아닙니다.")
