import time

def timer(second, callback):
    print("타이머 시작")
    print(f"{second}초 뒤에 요청한 함수를 호출합니다.")

    time.sleep(second)
    #time.sleep : time 모듈에 있는 기능(프로그램을 일정 시간 동안 멈추게 하는 함수)

    callback()
    print("타이머 종료")

def print_text():
    print("5초 뒤 실행될 함수 입니다. ")

timer(5,print_text)