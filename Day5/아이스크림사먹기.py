'''
우리가 가진 돈 : 5000원
아이스크림 1000원
아이스크림을 2번 사먹을 것
아이스크림을 1번 사먹었다! 남은 돈 ?? 원
아이스크림을 2번 사먹었다! 남은 돈 ?? 원
'''

icecream_count = 0
money = 5000
while icecream_count < 2:
    icecream_count += 1
    print(f"아이스크림을 {icecream_count}번 사먹었다! 남은돈 {money - icecream_count * 1000}원")
