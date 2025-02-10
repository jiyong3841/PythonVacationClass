'''
세트
1. 순서 X / 중복된 값 X

변수명 = {요소1, 요소2, 요소3}
set(세트로 바꾸고 싶은 다른 자료구조)
'''

# str = "apple"
# list = [1,2,3]
# tuple = (1,2,3)

print("각각의 자료구조들")
print("str : ", str)
print("list : ", list)
print("tuple : ", tuple)

set_str = set(str)
set_list = set(list)
set_tuple = set(tuple)

print("set 로 변한 자료 구조들")
print("set_str : ", set_str)
print("set_list : ", set_list)
print("set_tuple : ", set_tuple)

str_banana = "banana"
set_banana = set(str_banana)
print(str_banana[0])
# print(set_banana[0])

print()

list_banana = list(set_banana)
tuple_banana = tuple(set_banana)
print(list_banana)
print(tuple_banana[0])
# 세트 구조의 요소에 접근 하고 싶다면 리스트나 튜플로 변환 후 접근이 가능하다!