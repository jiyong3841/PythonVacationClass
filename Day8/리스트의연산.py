'''
리스트 결합
1. + 연산자
2. extend() : 기존 리스트에 추가
'''

list1 = ['a','b','c']
list2 =['d','e']

list3 = list1 + list2
print(list3)

list1.extend(list2)
print(list1)

# +는 새로운 리스트를 생성하기 때문에 기존의 리스트는 변하지 않는다
# extend() 메서드를 사용하면 기존 리스틍 새로운 리스트를 추가하여 리스트를 확장하는 기능(원본 변경됨)

list4 = list2 * 3
print(list4)

result = len(list4)
print(result)

#in 연산자 - True / False
print('d' in list4)

result2 = list4.count('e')
print(result2)

list5 = [99,45,61,216,54,21,54,78]
print(max(list5)) #최대값
print(min(list5))  #최소값