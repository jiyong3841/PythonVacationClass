'''

리스트 추가
1. append() : 리스트의 마지막에 새로운 요소를 추가
2. insert() : 리스트의 중간에 새로운 요소를 추가

리스트 삭제
1. remove() : 특정 값을 가진 요소를 삭제
2. pop() : 특정 위치에 있는 리스트를 삭제

리스트 정렬
1. sort() : 오름차순 정렬 (원본 리스트가 변경됨)
2. sort(reverse = True) 리스트를 내림차순으로 정렬
3. sorted() : 정렬된 새로운 리스트를 반환 (원본 리스트가 변경되지 않음)

리스트 반전
reverse() : 원본 리스트를 역순으로 변경

리스트 문자열
join() : 리스트 요소에 연결 문자를 추가해 하나의 문자열로 결합
'''

# append()
append_nums = [1,2,3]
print(f"append() 추가 전 : {append_nums}")
append_nums.append(4)
print(f"append() 추가 후 : {append_nums}")

#insert()
alphabets = ["a","b","c"]
print(f"insert() 추가 전 : {alphabets}")
alphabets.insert(1, "M")
print(f"insert() 추가 후 : {alphabets}")

#remove() - 인덱스 내 요소 입력
remove_nums = [1,2,3,4]
print(f"remove() 삭제 전 : {remove_nums}")
remove_nums.remove(2)
print(f"remove() 삭제 후 : {remove_nums}")
# remove_nums.remove(5)
# print(f"remove() 없는 값 삭제 : {remove_nums}")

#pop() - 인덱스 번호 입력
colors = ["red","black","yellow","black"]
print(f"pop() 삭제 전 : {colors}")
colors.pop(3)
print(f"pop() 삭제 후 : {colors}")

#reverse()
reverse_num = [2,8, 34, 24, 80]
print(f"reverse() 적용 전 : {reverse_num}")
reverse_num.reverse()
print(f"reverse() 적용 후 : {reverse_num}")

#join()
join_text = ["i","love","dog"]
print(f"join(-) 적용 전 : {join_text}")
join_result = "-".join(join_text)
print(f"join(-) 적용 후 : {join_result}")