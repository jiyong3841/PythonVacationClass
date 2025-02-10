'''
창고에 4종류의 과자가 있고 각각 10개 3개 0개 5개의 재고
0개라면 재고가 없습니다.
5개 미만이라면 재고가 부족합니다 현재 *개 남음
재고가 5개 보다 많다면 재고 충분! (현재 *개) 출력
items()
for 1,2 in 딕셔너리.items():
'''

storage = {
    'a' : 10,
    'b' : 3,
    'c' : 0,
    'd' : 5
}

for item, stock in storage.items():
    print(item)
    if stock == 0:
        print(f"{item}의 재고가 없습니다.")
    elif stock < 5:
        print(f"{item}의 재고가 부족합니다. 현재 {stock}개 남음")
    else:
        print(f"{item}의 재고 충분! (현재 {stock}개)")


