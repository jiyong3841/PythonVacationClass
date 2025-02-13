'''
1. 입력 : input 파일에서 데이터를 읽어옴
2. 출력 : output 데이터를 파일에 저장하거나 기록함

open("파일명","모드")
파일명이란? 작업할 파일의 이름
모드란?
1. "r" : 읽기모드 ( 파일을 읽기만 할 때)
2. "w" : 쓰기모드 (새로운 파일을 생성하거나 내용으 덮어쓸때)
3. "a" : 추가모드 ( 파일 끝에 데어터를 추가 )
'''

file = open ("example.txt", "r")
file.close()

'''
파일 읽기
1. 변수명.read() : 파일 전체 내용 읽기
2. 변수명.readline() : 파일 한 줄 읽기
3. 변수명.readlines() : 파일의 모든 줄을 읽어 리스트로 반환하기
'''

file2 = open("example.txt", "r", encoding="utf-8") #한글 출력 필요시 뒤에 encoding="utf-8" 입력
file_read = file2.read()
print(file_read)
file2.close()

#파일 존재여부 검사하는 방법
import os
print("파일 존재 여부 : ", os.path.exists("example.txt"))
print("파일 존재 여부 : ", os.path.exists("test.txt"))

file3 = open("text.txt", "w")
file3.write("Python Class")
file3.close()

