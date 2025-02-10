'''
학생 딕셔너리 만들기
딕셔너리의 값이 학생들이 좋아하는 과목 리스트일 것 (2가지)

어떤 과목을 좋아하는 학생을 찾을까요?

**학생이 **을(를) 좋아해요!
'''

student = {
    "짱구" : ["과학","수학"],
    "철수" : ["과학","영어"],
    "유리" : ["영어","수학"],
    "맹구" : ["국어","영어"]
}

found = False #과목을 찾았는지 여부를 결정할 변수

subject_input = input("어떤 과목을 좋아하는 학생을 찾을까요?")
for name, subject in student.items():
    if subject_input in subject:
        print(f"{name}학생이 {subject_input}과목을 좋아해요")
        found = True

if not found:
        print(f"입력하신 {subject_input}과목은 없는 과목입니다.")