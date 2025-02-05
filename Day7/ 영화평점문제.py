'''
영화 이름을 입력받고 영화 평점을 입력받을 것 (1~5)
1부터 5까지의 숫자를 입력하세요
영화 이름의 평점 :
continue/break
'''

name = input("영화 이름을 입력하세요 : ")
while True:
    num = int(input("영화 평점을 입력하세요 (1~5) : "))
    if 1<= num <=5:
        print(f"{name}의 평점 : " + "⭐" * num)
    else:
        print("다시 입력하세요")
        continue
    break
