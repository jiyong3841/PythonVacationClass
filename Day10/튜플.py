'''
튜플 -> 변수명 : (요소1, 요소2, 요소3) 튜플의 특성 : 불변
리스트 -> 변수명 : [요소1, 요소2, 요소3]
'''
from distutils.command.build_scripts import first_line_re

alphabets = ('a','b','c') # 문자
colors = ("red","orange","yellow") # 문자열
bools_tuple = (True, False, True) # 논리값
mix_tuple = ("red", 'g', 3, True) # 혼합

names = ("choi", "ji", "yong")
first_name = names[0]
second_name = names[1]
third_name = names[2]

print(first_name)
print(second_name)
print(third_name)

first_name2 = names[-3]
print(first_name2)

num_list = [1,2,3]
num_tuple = (1,2,3)

print(num_list)
print(num_tuple)

num_list[0] = 100
print(num_list)

# num_tuple[0] = 100
# print(num_tuple)

num_list.append(4)
print(num_list)

# num_tuple.append(4)
# print(num_tuple)

'''
튜플의 장점
1. 데이터의 손상을 방지
2. 코드의 안정성 향상 
'''

#튜플의 중첩
multi_tuple = (1,(2,3),[4,5])
print(multi_tuple[2])
print(multi_tuple[1][1])
print(multi_tuple[0])

multi_tuple[2][0] = 3
print(multi_tuple[2])
#튜플 안에 있는 리스트는 수정이 가능하다

#튜플 슬라이싱
slice_tuple = (3,10,"파이썬", True, "고양이", 23)
print(slice_tuple[1:4])
print(slice_tuple[:5])
print(slice_tuple[0:8])
print(slice_tuple[8:20])

#튜플 메서드
'''
1. count() : 튜플에서 특정 값이 몇 번 등장했는지 카운트함
2. index() : 튜플에서 특정 값이 처음 등장하는 위치(인덱스)를 반환함
'''

my_tuple = (1,2,3,2,2,4)
count_of_2 = my_tuple.count(2)
print(count_of_2)

my_tuple2 = (10,20,30,20,40)
index_of_20  = my_tuple2.index(20)
print(index_of_20)

'''
자주 사용 하는 것
1. len() : 길이
2. in : 요소 포함 여부 확인
3. +연산자 : 튜플끼리 병합
4. *연산자 :튜플 반복
'''

my_tuple3 = (1,2,3,4)
print(len(my_tuple3))
print(5 in my_tuple3)

t1 = (1,2)
t2 = (3,4)
print(t1 + t2)
t3 = t1 * 3
print(t3)

a = 10
b = 20
print(f"교환 전 -> a = {a} / b = {b}")
a,b = b,a
print(f"교환 후 -> a = {a} / b = {b}")
# 튜플은 데이터를 변경하거나 추가하지 못하지만 데이터를 교환하는 방식으로 사용하거나 변수를 바꾸는 데 활용 가능