str_random = "aodnaownoanwgiwbibribdcozcboiuqewpruoizdafslh"

str_random = set(str_random)
print(str_random)

sorted_list_change = sorted(str_random)
print(sorted_list_change)
print(str_random)

list_str = list(str_random)
print(list_str)
list_str = list(str_random)
print(list_str)
list_str.sort()
print(list_str)
print(f"3번째로 작은 알파벳은 {list_str[2]} 입니다.")