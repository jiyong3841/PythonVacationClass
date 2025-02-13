'''
클래스 : 설계도 (속성, 메서드)
속성 : 클래스 내부에 정의된 변수로 객체가 가지는 데이터
메서드 : 클래스 내부에 정의된 함수로 객체가 수행할 수 있는 행동을 정의함

객체
클래스를 통해 만들어진 사물 -> 휴대폰, tv, 사람, 책 등등
특징
1. 상태 (state) : 학생이라면 이름, 나이, 학과
2. 행동 (behavior) : 특정한 기능, 행동을 수행할 수 있다. 학생이라면 공부, 운동 책읽기 등

class 클래스명:
    클래스변수
    생성자
    메서드
* 클래스 정의할 때 주의사항
    1. 클래스 이름은 대문자로 시작한다.
    2. 클래스 내부에 메서드(함수)나 속성을 추가해서 동작을 정의한다.

속성 정의하기 : __init__
    * 객체가 생성될 때 자동으로 호출되는 생성자이다.
    * 생성자에서 객체의 초기상태(속성)을 설정한다.
    * 항상 첫 매개변수로 전달된다.

행동 정의하기(메서드 추가)
    * 메서드는 클래스가 제공하는 기능(행동)을 정의한다.
    * 메서드도 항상 self를 첫 매개변수로 사용한다.

self ? 현재 생성되는 객체 자신을 가리키는 변수
'''

class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def introduce(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 국적 : {self.nationality}")

# 객체 생성
person1 = Person("홍길동",10,"Korea")
person2 = Person("김철수", 12, "Korea")

print(person1.name)
print(person2.age)

person1.introduce()

'''
메서드와 함수의 차이점
함수 
선언부 : 클래스 밖에서 정의됨 
호출 방법 : 함수이름()
self필요 : X

메서드
선언부 : 클래스 안에서 정의됨 
호출 방법 : 객체이름.함수이름() -> 클래스(설계도)를 활용하여 만들어낸 객체가 가질 수 있는 기능 
self필요 : O
'''



