'''
딕셔너리 생성
flower = 꽃
food = 음식
car = 차
cat = 고양이

사용자한테 영어 단어 입력
사용자가 입력한 단어가 딕셔너리에 있는지 확인
사용자가 입력한 단어가 있다면 출력
사전에 없으면 단어의 뜻을 입력해 주세요 입력한 단어와 뜻을 딕셔너리에 추가
'''

english_dict = {
    "flower" : "꽃",
    "food" : "음식",
    "floor" : "바닥",
    "sky" : "하늘"
}

user_word = input("영어 단어를 입력해 주세요 : ")

if user_word in english_dict:
    print(f"{user_word} : {english_dict[user_word]}")
else:
    print(f"{user_word}는 사전에 없습니다.")
    add_value = input("단어의 뜻을 입력하세요 : ")
    english_dict[user_word] = add_value
    print(f"{user_word} : {english_dict[user_word]} (사전에 추가되었습니다!)")