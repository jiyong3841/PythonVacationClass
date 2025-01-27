'''
아이디
비밀번호
아이디 영문이름 비밀번호 1234
'''

ID = "Jiyong"
PW = 1234
id = input("아이디를 입력하세요 : ")
pw = int(input("비밀번호를 입력하세요 : "))

if ID == id and PW == pw :
    print("로그인 되었습니다.")
elif ID != id and PW == pw :
    print("아이디 불일치")
elif ID == id and PW != pw :
    print("비밀번호 불일치")
else:
    print("아이디 비밀번호 불일치! 회원가입 하러가기")
