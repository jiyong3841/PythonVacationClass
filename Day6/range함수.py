#1~5
#1+2+3+4+5
'''
sum = 0
sum += 1
sum += 2
sum += 3
sum += 4
sum += 5
'''

nums = [1,2,3,4,5]
sum = 0
for nums_for in nums:
    sum += nums_for
print(sum)

'''
for 변수 in range(start, stop, step)
    실행할 코드
'''

for range_for in range(5):
    print(range_for)

print()

for range_for2 in range(2,6):
    print(range_for2)
#시작값은 작성하지 않으면 0
#작성하면 작성 숫자 포함
#끝나는 값은 포함X

print()

for range_for3 in range(1,10,2):
    print(range_for3)

print()

for range_for4 in range(10,0,-2):
    print(range_for4)

#1~5까지의 합을 ragne를 이용해 출력

print()

sum1= 0
for range_for5 in range(1,6):
    sum1 += range_for5
print(sum1)

print()

fruits = ["apple", "banana", "cherry"]
for range_for6 in range(len(fruits)):
    print(f"인덱스 {range_for6} : {fruits[range_for6]}")

