'''
매개변수
def 함수이름(매개변수1, 매개변수2...):
    기능 코드 작성
'''

def candy_fluff(count):
    print("오늘은 솜사탕을 " +str(count) + "개 만들어야 합니다.")


candy_fluff(15)
# 매개 변수가 있는 함수를 선언 했다면 호출할 때 매개 변수 값을 넣어 주어야 한다.
candy_fluff(2)

'''
블랭핑크가 자기소개 하는 함수 만들고 호출하기
'''

def hello(name):
    print(f"안녕하세요 제 이름은 {name}입니다")

hello("지수")
hello("제니")

def plus(a,b):
    print(a+b)
plus(10,20)
plus(20,5)

