'''
예외
1. 에러 : 프로그램 오류 또는 시스템 문제가 발생하는 예외 ( 개발자가 직접 해결해야함 )
2. 예외 : 사용자의 입력에 따라 발생하는 예외
'''

# print(7/0) - 에러

# num1 = int(input("첫 번째 정수를 입력 : "))
# num2 = int(input("두 번째 정수를 입력 : "))
#
# if(num2 == 0):
#     print("0으로 나눌 수 없습니다.!")
# else:
#     print(f"num1 나누기 num2의 결과는 : {num1/num2}입니다. ")

''' 외울필요는없음
예외 처리 클래스
1. BaseException : 최상위 예외 클래스   
2. Exception : 대부분 예외 클래스의 슈퍼 클래스
3. ArithmeticError : 산술 연산 오류
    - OverflowError : 산술 연산의 결과가 너무 커서 표현할 수 없을 때
    - ZeroDivisionError : 0으로 나누려고 할 때
    - FloatingPointError : 실수 연산에서 오류가 발생할 때
4. AttributeError : 잘못된 속성 참조
5. EOFError : 파일에서 더이상 읽을 데이터가 없음
6. ModuleNotFoundError : Import할 모듈이 없음
7. FileNotFoundError : 존재하지 않는 파일
8. IndexError : 잘못된 인덱스 사용
9. NameError : 잘못된 이름(변수) 사용
10. SyntaxError : 문법 오류 
11. TypeError : 계산하려는 데이터의 유형 오류 (서로 다른 타입끼리 계산하려 할때)
12. ValueError : 계산하려는 데이터의 값 오류
'''

'''
try-except
try:
    예외가 발생할 수 있는 코드
except: 
     예외가 발생했을 때 수행하는 코드
'''

# try:
#     num1 = int(input("첫 번째 정수를 입력 : "))
#     num2 = int(input("두 번째 정수를 입력 : "))
#     print(f"{num1} 나누기 {num2}는 {num1/num2}입니다. ")
#
# except ArithmeticError:
#     print("산술연산 예외가 발생했습니다.")
# except ValueError:
#     print("입력값 예외가 발생했습니다.")

'''
리스트 만들기 - 숫자 4가지
인덱스 에러를 발생시켜서 인덱스 범위를 벗어났습니다. 출력
'''

try:
    list = [1,2,3,4]
    print(list[4])

except IndexError:
    print("인덱스 범위를 벗어났습니다. ")

#try-except as 예외 메세지 변수
try:
    num1 = int(input("첫 번째 정수를 입력 : "))
    num2 = int(input("두 번째 정수를 입력 : "))
    print(f"{num1} 나누기 {num2}는 {num1/num2}입니다. ")

except ArithmeticError as e:
    print(f"산술연산 예외가 발생했습니다. 상태메세지는 {e}입니다.")
except ValueError as E:
    print(f"입력값 예외가 발생했습니다. 상태메세지는 {E}입니다.")