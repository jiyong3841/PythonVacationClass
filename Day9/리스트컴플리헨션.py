'''
새 리스트 = [표현식 for 변수 in 반복할리스트 if 조건]

표현식 : for문을 돌면서 새로운 리스트에 추가될 값을 결정
'''

numbers = []
for i in range(1,11):
    numbers.append(i)
print(numbers)

number = [i+1 for i in range(1,11)]
print(number)

even_numbers = [i for i in range(1,11) if i % 2 == 0]
print(even_numbers)

result  = []
for i in range(1,6):
    if i %2 == 0:
        result.append("짝수")
    else:
        result.append("홀수")
    print(result)

    result2 = ["짝수" if i % 2 ==0 else "홀수"for i in range(1,6)]
    print(result2)

    num_list = [
        [1,3,5],
        [6,9,12],
        [15, 18,21]
    ]
    multipls_of_three = [num for row in num_list for num in row if num %3 == 0 ]
    print(multipls_of_three)