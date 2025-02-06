'''
여러가지 숫자가 있는 리스트에서 5이상인 숫자만 비어있는 리스트에 추가하고 오름차순으로 변경해서 출력
3,7,8,6,10,4,2,5,0,1
'''

'''
.sort()#오름차순
.sort(reverse=True)#내림차순
#append(): 리스트 끝에 요소를 추가하는 메서드
'''


list1 = [3,7,8,6,10,4,2,5,0,1]
list2 = []
for num in list1:
    if num >= 5:
        list2.append(num)
list2.sort()
print(list2, end="")

