'''
th__del__()
객체가 더이상 사용되지 않고 메모리에서 제거되기 전에 마지막으로 사용하는 코드를 뜻함
'''

class FileHandler:
    def __init__(self,filename):
        self.file = open(filename, 'w')
        print(f"{filename} 파일을 열었습니다. ")

    def write_data(self,data):
        self.file.write(data)

    def __del__(self):
        self.file.close()
        print("파일을 닫았습니다.")
'''
1. 파일을 닫는 경우
2. 데이터베이스 연결 해제
3. 네트어크 연결 종료 
'''
handler = FileHandler("fileHandler_text.txt")
handler.write_data("www python")
# del handler