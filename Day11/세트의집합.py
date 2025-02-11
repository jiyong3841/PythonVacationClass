# 세트의 교집합
'''
1. & 연산자 사용 : 두 세트를 & 연산자로 연결하여 새로운 새트를 만들며, 이 때 중복되는 요소는 제거한다.
2. intersection() 메서드 사용 : 두 세트를 인자로 전달하여 교집합을 반환
'''
print("교집합")


set_a = {1,2,3,4}
set_b = {3,4,5,6}
print(set_a)
print(set_b)

intersection_a_b = set_a.intersection(set_b)
print(intersection_a_b)

a_and_b = set_a & set_b
print(a_and_b)

'''
과일바구니 : strawberry orange cherry
내가 좋아하는 과일 : grape orange strawberry
'''

set_fruits = {"strawberry", "orange", "cherry"}
set_favorites = {"grape", "orange", "strawberry"}

and_fruits = set_fruits & set_favorites
print(and_fruits)

intersection_fruits_favorites = set_fruits.intersection(set_favorites)
print(intersection_fruits_favorites)

print()

# 세트의 합집합
'''
1. | 연산자 사용
2. union() 메서드 사용
'''

print("합집합")


set_c = {1,2,3}
set_d = {3,4,5}

pipe_set = set_c | set_d
print(pipe_set)

union_set = set_c.union(set_d)
print(union_set)

'''
수학반 : 엘사, 모아나, 라푼젤
과학반 : 엘사, 안나, 모아나
'''
student_math = {"엘사", "모아나","라푼젤"}
student_science = {"엘사", "안나", "모아나"}

all_student = student_math | student_science
print(all_student)

all_student_union = student_math.union(student_science)
print(all_student_union)

print()
print("차집합")

# 세트의 차집합
'''
1. - 연산자 사용
2. difference()
'''

set_e = {1,2,3,4}
set_f = {3,4,5,6}

minus_set = set_e - set_f
print(minus_set)

diff_set = set_e.difference(set_f)
print(diff_set)

'''
음악반 학생 : 알라딘 오로라 자스민
역사반 학생 : 오로라 자스민
음악만 공부하는 학생 출력하기
'''

class_music = {"알라딘", "오로라", "자스민"}
class_history = {"오로라", "자스민"}

diff_class = class_music.difference(class_history)
print(diff_class)

