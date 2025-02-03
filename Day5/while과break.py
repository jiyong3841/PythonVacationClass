'''
시작 숫자는 0
숫자는 30까지 증가할것
5의 배수는 출력하지 않으며, 짝수도 출력하지 않는다
break countinue 둘다 사용하기
'''

num = 0
while num < 30:
    num += 1
    if num % 5 == 0:
        continue
    if num % 2 == 0:
        continue
    if num > 26:
        break
    print(num, end=" ")