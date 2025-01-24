'''
1. and : 연산자를 기준으로 왼쪽과 오른쪽 갑시 모두 true일때만 True를 반환
2. or : 연산자를 기준으로 왼쪽과 오른쪽 값 중 하나라도 True 이면 True를 반환
3. not : 뒤에 따라오는 논리값이 True이면 False 반환(반대로 출력)
        True 라면 False를 False라면 True를 반환
'''

num1 = 10
num2 = 20
num3 = 30

num_result = num1 < num2 and num2 < num3
print(num_result)

num_result2 = num1 > num2 and num2 < num3
print(num_result2)

num_result3 = num1>num2 or num2<num3
print(num_result3)

num_result4 = num1>num2 or num2>num3
print(num_result4)

false = False
print(false)
print(not false)
print(false)

'''
빈 문자열을 선언 후 
해당 문자열이 비어있다면 True를 출력하는 프로그램 만들기
'''

text = ""
print(not text)

'''
15라는 숫자가 10이상 이하인지 확인
'''
num = 15
result = num >= 10 and num <= 20
print(result)