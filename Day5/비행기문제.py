'''
비행기는 총 3대 운항할것
프로그램을 실행하면 (1번째 비행기 탑승 준비!) 출력
비행기는 여권을 가진 사람이 2명이 탑승하면 출발

승객에게 질문 *번째 고객님 여권이 있나요? (yes, no)
여권이 없다면 (여권이 없어요! 다음 승객 기다리기... )출력후 다음 승객에게 다시 여권 유무 묻기
여권 있는 승객이 타면 *번째 승객이 탑승했습니! 출력후 한명만 탔으니 다시 여권 유무 묻는 반복 실행
여권을 가지 ㄴ2명이 나타나서 승객이 다 채워지면 비행기 출발 후 다음 비행기 운항 출력
'''

flight = 0
while flight < 3:
    flight += 1
    print(f"{flight}번째 비행기 탑승 준비!")
    passenger = 1
    count_num = 0

    while count_num < 2:
        answer = input(f"{passenger}번째 고객님 여권이 있나요? (yes or no)")

        if answer == "yes":
            print(f"{passenger}번째 승객이 탑승했습니다.")
            count_num += 1
        else:
            print("여권이 없어요 다음 승객 기다리기...")
        passenger += 1

    print(f"{flight}번째 비행기 출발!")


