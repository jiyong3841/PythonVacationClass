'''
사용자에게 키와 나이를 입력받아 키가 120이상이고 나이가 열살 이상이어야만 놀이기구를 탈 수 있다
'''

height = input("사용자의 키를 입력하세요 : ")
age = input("사용자의 나이를 입력하세요 : ")

result = int(height) >= 120 and int(age) >= 10
print(f"놀이기구를 탈수 있나요?{result}")
