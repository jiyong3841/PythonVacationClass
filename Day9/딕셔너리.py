'''
딕셔너리 : 키와 쌍으로 이루어지 데이터 구조

key1 : value1
key2 : value2
'''

me = {
    "name" : "Jiyong",
    "age" :  20,
    "phone" : "010-3841-4270",
    "class" : ["c언어", "python","java"] # 값을 리스트로도 가질 수 있다.
}

print(me)
print(me["phone"])

#폰에 대한 딕셔너리
#키 : name / price / color / storage

phone = {
    "name" : "samsung",
    "price" : 1000000,
    "color" : "black",
    "storage" : "512GB"
}
print(phone)

friends = {}
friends["도현"] = 19
friends["길동"] = 27
print(friends)
print(friends["길동"])
friends["도현"] = 29
print(friends["도현"])

del friends["길동"]
print(friends)

friends.clear()
print(friends)