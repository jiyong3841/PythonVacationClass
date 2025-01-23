# 학번입력받기

# 1번째 숫자는 학년
# 2번째 숫자는 반
# 3번째 숫자는 번호
# *학년 *반 *번
student_id = input("4자리 학번을 입력하세요 : ")
print(student_id)
slice1 = student_id[0]
slice2 = student_id[1]
slice3 = student_id[2:4]

print(f"{slice1}학년 {slice2}반 {slice3}번")