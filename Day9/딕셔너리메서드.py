'''
1. key() : 딕셔너리의 모든 key 값을 모아서 반환
2. value() : 딕셔너리의 모든 값을 반환
3. items() : 딕셔너리의 모든 키(key)값과 값(value)를 반환  (쌍을 반환) *튜플
4. update(other_dict) : 딕셔너리에 다른 딕셔너리의 키 - 값 쌍을 추가하거나 덮어씀
'''

print("key()")
my_dict = {
    "name" : "Kelly",
    "age" : 25,
    "city" : "New York"
}
keys = my_dict.keys()
print(keys)

lists = list(my_dict.keys())
print(lists)

print()

print("value()")
values = my_dict.values()
print(values)

print()

print("items()")
items = my_dict.items()
print(items)

print()

print("update()") #키가 원래 딕셔너리에 있다면 값이 덮어 씌워짐 키가 없다면 새로 추가됨
my_dict.update({"age" : 26, "hobby" : "freeDiving"})
print(my_dict)

print()
#키값을 기준으로 오름차순 내림차순이 정렬됨
print(sorted(my_dict,reverse=True))
print(sorted(my_dict.items()))

