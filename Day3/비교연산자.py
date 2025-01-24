'''
1. a > b : a가 b보다 크다
2. a < b : a가 b보다 작다
3. a >= b : a가 b보다 크거나 같다
4. a <= b : a가 b보다 작거나 같다
5. a == b : a와 b는 같다 (= : 대입연산자)
5. a != b : a와 b는 다르다

맞으면 ture, 틀리면 false
'''

a = 10
b = 7
ab_result = a > b
print(ab_result)

ab_result2 = a < b
print(ab_result2)

ab_result3 = a >= b
print(ab_result3)

ab_result4 = a <= b
print(ab_result4)

ab_result5 = a == b
print(ab_result5)

ab_result6 = a != b
print(ab_result6)

#문자열 비교

string1 = "Python"
string2 = "P" + "y" + "t" + "h" + "o" + "n"

string_result = string1 ==string2
print(string_result)

#문자열, 숫자형 비교
one =1
first = "1"
type_result = one == first
print(type_result)

#다중연산자
x = 1
y = 2
z = 3
xyz_result = x < y < z
print(xyz_result)