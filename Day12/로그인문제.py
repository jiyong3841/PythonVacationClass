'''
1. 정해진 아이디와 비밀번호를 만들어 놓기
2. 함수를 만들어 두개의 매개변수를 받을 것! (id, pw)
3. 매개변수로 받은 아이디와 정해진 아이디가 일치하고 비번도 일치하면 로그인 되었습니다.
4. 아이디 맞고 비번을 틀림 = 비번 불일치
4. 아이디 틀림 아디디 불일치
'''

right_id = "jiyong"
right_pw = 1234

def login(id,pw):

    if id == right_id:
        if pw == right_pw:
            print("로그인 되었습니다.")
        else:
            print("비밀번호 불일치")
    else:
        print("아이디 불일치")


user_id = input("아이디를 입력해 주세요 ")
user_pw = (int)(input("비밀번호를 입력해 주세요 "))
login(user_id,user_pw)
