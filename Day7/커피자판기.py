'''
무한 반복하는 반복문을 생성한다 커피를 뽑는 자판기를 만든다
커피는 한잔에 300원 사용자가 돈을 ??원 넣으면 몇잔 뽑는지 물어본다
입력받은 돈이 300원보다 크면 최대 **잔을 뽑을 수 있다고 알려준다
커피를 뽑을 때 사용자는 최소 300원 이상을 입력해야 하고 300원 이하로 입력했다면 300원 이상 넣어달라는 문구를 작성하고 돈을 다시 받는다

사용자가 낸 돈보다 더 많은 양의 커피를 뽑으려 하면 최대 **잔까지 뽑을 수 있습니다. 출력후 다시 개수 입력받음
사용자가 입력한 돈에서 커피 개수와 커피 값을 연산하여 차감한 후 (잔돈계산)
커피 **잔을 뽑았습니다. 잔돈 **원 출력
잔돈이 300원 이상이라면 자판기 반복 이하라면 자판기 종료
'''

total_money = 0
while True:
    money = int(input(f"돈을 넣어주세요 (300원 이상) (현재 잔돈 : {total_money}) : "))
    total_money += money #입력받은 돈과 잔돈과 합산

    if total_money <300:
        print("돈을 더 넣어주세요")
        continue #다시 반복으로 돌아가기

    coffee_price = 300 #커피 한 잔 가격
    max_coffee = total_money // coffee_price

    while True:
        print(f"최대 {max_coffee}잔 가능합니다. (잔돈 포함)")
        coffee_count = int(input("커피를 몇잔 뽑을지 입력해주세요"))

        if coffee_count > max_coffee:
            print(f"잔돈이 부족합니다. 최대 {max_coffee}잔까지 가능합니다.")
        elif coffee_count <= 0:
            print("1잔 이상 입력해주세요")
        else:
            break

    total_money -= coffee_price * coffee_count
    print(f"커피 {coffee_count}잔을 뽑았습니다. 남은 잔돈 {total_money}")

    if total_money <300:
        print("잔돈이 부족하여 종료합니다")
        break

