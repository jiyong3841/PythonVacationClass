from flask import Flask

from urllib import request
from bs4 import BeautifulSoup
news_url = "https://www.korea.kr/rss/policy.xml"

app = Flask(__name__)
@app.route("/") #기본 url
def hello():
    return "<hi>웹서버 생성 완료</hi>"

@app.route("/news")
def news():
    # return "<hi>기사 크롤링 완료</h1>"
    output = ""
    response = request.urlopen(news_url)
    xml = response.read()
    soup = BeautifulSoup(xml, "xml")

    # data = request.urlopen(news_url)
    # with request.urlopen(news_url) as response:
    #     soup = BeautifulSoup(response, "xml")

    items = soup.select("item")  # 특정 이름을 가진 태그를 모두 찾아줌
    title = soup.select_one("title").text  # 특정 이름을 가진 태그를 하나만 찾아줌
    output += f"<h1>{items}{title}</h1>"
    return output

if __name__ == "__main__":
    app.run(debug=True)

