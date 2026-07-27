age = -5
if age <= 0:
    raise ValueError("나이가 0이거나 작을 수 없다")
print("나이:", age)

try:
    age = int(input("나이를 입력하세요"))
    if age <= 0:
        raise ValueError("나이가 0이거나 작을 수 없다")
except ValueError as e:
    print("오류발생", e)
else:
    print("나이:", age)
finally:
    print("실행 종료")