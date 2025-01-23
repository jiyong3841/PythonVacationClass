name1 = "choi"
name2 = 'ji yong'
name3 = '''choi ji yong'''
name4 = """ji yong choi"""

num = "100"
null_string = "" #False로 간주한다

str1 = "Park's Bakery"
str2 = 'eunji say "so happy"'
print(str2)

# 문자열 연산
first_name = "Choi"
last_name = "Ji Yong"
full_name = first_name + last_name
print(full_name)

class_name = 'python '
print(class_name)
print(class_name * 5)
# 문자열 연산에서는 +와 *만 가능하다

a = "apple"
first_char = a[0]
third_char = a[3]
print(first_char)
print(third_char)

#마이너스 인덱스 : 문자열의 뒤에서부터 인덱스 번호를 부여하는 방식
last_char = a[-1]
print(last_char)
last_char2 = a[-3]
print(last_char2)

#문자열 슬라이싱
#변수명[start:stop:step] : 문자열 슬라이스의 기본 구조
'''
start (시작 인덱스) : 슬라이싱을 시작할 위치 정하기 (생략하면 0)
stop (종료 인덱스) : 슬라이싱을 종료할 인덱스번호 +1 (생략가능, 생략하면 마지막 인덱스 +1)
step (증감폭) : 인덱스의 증가 또는 감소값을 지정, 기본값은 1이며 생략하면 1씩 증감
'''

text = "I Love Pasta"
slicing1 = text[2:6] # 인덱스 번호 2부터 6-1(5)까지 출력
slicing2 = text[7:12]
print(slicing1)
print(slicing2)

steping = text[7:12:2]
print(steping)

first_lost = text[:6]
print(first_lost)
last_lost = text[6:]
print(last_lost)

#문자열 길이 len()
python_text = "Python"
python_length = len(python_text)
print(python_text)
print(python_length)
'''
length 외 유용한 함수
1. 문자열을 대문자로 변환 upper()
2. 문자열을 소문자로 변환하는 lower()
3. 양 끝 공백을 제거하는 strip()
'''

pizza = "i love pizza"
upper_pizza = pizza.upper()
print(upper_pizza)
lower_pizza = upper_pizza.lower()
print(lower_pizza)

coffee = "------This is coffee"
strip_coffee = coffee.strip("-")
print(strip_coffee)