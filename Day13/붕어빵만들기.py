'''
붕어빵 클래스를 만들것
맛과 개수를 생성자로 생성할 것
붕어빵이 만들어지면 붕어빵 클래스의 메서드로 **맛 붕어빵 **개 나왔습니다~! 출력

붕어빵을 만들어달라고 할때 어떤 맛 몇개 전달할 것임
'''

class Bungeobbang:
    def __init__(self,taste,count):
        self.taste = taste
        self.count = count

    def making(self):
        print(f"{self.taste}맛 붕어빵 {self.count}개 나왔습니다~!")

order1 = Bungeobbang("피자",3)
order2 = Bungeobbang("팥", 2)
order3 = Bungeobbang("슈크림", 1)

order1.making()
order2.making()
order3.making()

