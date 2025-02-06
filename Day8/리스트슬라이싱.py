'''
list[start:end:step]
start : 슬라이싱이 시작되는 인덱스(포함)
end : 슬라이싱이 끝나는 인덱스(포함되지 않음)
step : 요소를 건너뛰는 간격 (기본값 : 1)
'''

numbers = [10,20,30,40,50]
print(numbers[0:3])
print(numbers[1:4])
print(numbers[-2:])
print(numbers[ :-2])
print(numbers[::2])
print(numbers[::-1])

numbers[:2]= [100,200]
print(numbers)

numbers[:2] = []
print(numbers)