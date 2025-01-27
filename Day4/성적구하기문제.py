'''
점수 입력받기
90점 이상이면 A학점 참 잘했어요
80 이상이면 B
70 이상이면 C
F학점으로 재시험
'''

score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print(f"{score}점은 A학점 참 잘했어요")
elif score>=80:
    print(f"{score}점은 B학점입니다")
elif score>=70:
    print(f"{score}점은 C학점입니다")
else :
    print(f"{score}점은 F학점으로 재시험입니다.")


'''
좋아하는 달을 입력 받음
3,4,5 = 봄
6,7,8  = 여름
9,10,11 = 가을
12,1,2 = 겨울
'''

Month = int(input("1월부터 12월 중 좋아하는 달을 입력하세요 : "))
if 3<=Month<=5:
    print(f"{Month}월은 봄입니다.")
elif 6<= Month <= 8:
    print(f"{Month}월은 여름입니다.")
elif 9<=Month<=11:
    print(f"{Month}월은 가을입니다.")
else :
    print(f"{Month}월은 겨울입니다.")
