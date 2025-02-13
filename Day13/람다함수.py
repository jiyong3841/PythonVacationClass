'''
람다함수 : 익명함수

일반 함수
def 함수이름(매개변수):
    return 결과
=========================

람다 함수
lamda 매개변수: 결과
'''

def add(x,y):
    return x + y
print(add(5,1))

lambda_function = lambda k,f : k+f
print(lambda_function(5,5))

numbers = list(range(20))
print(numbers)

even_number = list(filter(lambda x: x % 2 == 0, numbers))
print(even_number)
#filter(function, iterable) : 조건에 맞는 요소만 걸러주는 함수
#function 조건 만족한다면 true 불만족 false

# 람다정렬

list_in_tuple = [(1,10),(4,2),(99,6),(5,1),(8,12),(-3,20)]
sorted_tuple = sorted(list_in_tuple)
print(sorted_tuple)

sorted_tuple2 = sorted(list_in_tuple, key=lambda index:index[1])

print(sorted_tuple2)