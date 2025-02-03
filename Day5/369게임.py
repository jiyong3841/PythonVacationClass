'''
초기값 : 0
반복문을 사용하여 10까지 증가
3의 배수라면 "짝"을 출력
'''

num = 0

while num < 10:
    num += 1
    if(num % 3 == 0):
        print("짝")
        continue
    print(num)