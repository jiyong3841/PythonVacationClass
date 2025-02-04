'''
range를 사용하여 구구단 2단 출력
'''

num1 = 2
for range_for in range(1,10):
    print(f"{num1} * {range_for} = {num1 * range_for}")

print()

for x in range(2,10):
    for y in range(1,10):
        print(f"{x} X {y} = {x * y}")
    print()

    '''
    반복문의 종류에는 while, for
    break / continue
    '''
