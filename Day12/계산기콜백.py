'''
숫자 2개와 연산자를 받는 함수 생성 -> 연산자(매개변수1, 매개변수2)
1. 더하기
2. 빼기
3. 곱하기
4. 나누기 함수
'''

def calculator(x, y, operation):
    return operation(x,y)

def plus(x,y):
    return x + y

def minus(x,y):
    return x - y

def multiple(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "0으로 나눌 수 없습니다."
    return x / y

plus_result = calculator(2,6,plus)
minus_result = calculator(2,6, minus)
multiple_result = calculator(2,6,multiple)
divide_result = calculator(30,6, divide)

print(plus_result)
print(minus_result)
print(multiple_result)
print(divide_result)



