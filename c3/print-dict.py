# 딕셔너리형 데이터(과일 이름과 가격)을 변수에 대입
fruits = {
    "바나나": 3000,
    "오렌지": 2400,
    "딸기": 3500,
    "망고": 4000
}

# 딕셔너리 데이터 목록을 표시
for name in fruits.keys():
    # 가격을 얻는다
    price = fruits[name]
    # 화면에 출력한다
    s = "{0}는 {1}원입니다.".format(name, price)
    print(s)
