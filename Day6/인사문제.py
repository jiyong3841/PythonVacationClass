'''
정수를 입력바당 입력받은 회수만큼 *번째 안녕하세요 라고 출력하기
0보다 이하의 수가 입력되면 잘못된 입력입니다. 출력
'''

num = int(input("정수를 입력하세요 : "))

if num <= 0:
    print("잘못된 입력입니다.")
else:
    for n in range(num):
        print(f"{num}번째 안녕하세요")