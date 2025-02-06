'''
num = 7 원래 사용하던 변수
nums = [1,2,3,4] 여러개의 변수를 한꺼번에 생성
'''

number = [0,1,2,3] # 숫자리스트
alphabet = ['a','b','c'] #문자리스트
bools = [True, False,True] #논리값리스트
greetings = ["hello", "오늘은 파이썬", "8일차"] #문자열 리스트

mixed = [1, 'apple', 3.14, True] #혼합리스트
print(mixed)
print(mixed[1])

mixed[1] = 'mango'
print(mixed[1])

num_list = [54,456,12,45,30,341,45]
num_list.sort()#오름차순
print(num_list)
num_list.sort(reverse=True)#내림차순
print(num_list)

korean = ["가","가","가","나","차","하","라","마","바","사"]
korean2 = sorted(korean)

print(korean2) #오름차순
print(korean)
print(set(korean))
'''
sort : 오름차순 (기존 리스트 변경됨)
sorted : 기존 리스트 변경 없이 오름차순
sort(reverse = True) : 역순으로 출력하겠다 -> 내림차순
set() 중복 제거

'''