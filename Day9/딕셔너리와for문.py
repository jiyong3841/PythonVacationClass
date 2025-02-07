fruit_colors = {
    "Red" : "apple",
    "Yellow" : "banana",
    "Purple" : "blueberry"
}

#키값 출력
keys = fruit_colors.keys()
print(keys)

for i in fruit_colors.keys():
    print(i)

lists = list(fruit_colors.keys())
print(lists)

lists.append("Pink")
print(lists)