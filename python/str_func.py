class SimpleBook:
    def __init__(self,title,price):
        self.title = title
        self.price = price
    def __str__(self):
        return f"도서명: {self.title}, 가격: {self.price}"

s = SimpleBook()
print(s)
#s라는 객체를 출력하려고 하면 자동으로 __str__메서드 호출
#__str__메서드: 원하는 퍼맷으로 출력을 원할 때 사용 
        