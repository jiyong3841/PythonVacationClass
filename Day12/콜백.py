def hello(name):
    print(f"안녕! {name} :-)")

def call_function_with_name(callback,name):
    #callback : 다른 어떤 함수가 들어올 것
    callback(name) #전달받은 함수를 실행
    # callback(name) : callback이라는 함수에 name이라는 매개변수를 전달해라
    # hello(name)

call_function_with_name(hello,"지용")