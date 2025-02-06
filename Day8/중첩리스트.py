list_in_list = [1,[2,3],"hello",[True,False]]
#list_in_list = [1,                 0
                # [2,3],            1
                # "hello",          2
                # [True,False]]     3
print(list_in_list[1][1])

python_class = [
    ["철수","영희","민수"],    #1조
    ["지수","현우","나영"],   #2조
    ["동현","수진","호영"]    #3조
]

print(python_class[0])
print(python_class[1])
print(python_class[2])
print(python_class[2][1])

python_class[1][0] = "제니"
print(python_class[1][0])