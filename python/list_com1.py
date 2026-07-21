#comprehension: 반복문과 조건문을 한 줄로 간단하게 작성하여 딕셔너리, 세트를 만드는 방법

# 1. 리스트  컴프리헨션
# [저장할_값(표현식) for 변수 in 반복할_데이터]

#일반 반복문
numbers=[] #빈 리스트
for i in range(1,6):
    numbers.append(i)
print(numbers)

# 리스트  컴프리헨션
numbers = [i for i in range(1,6)]
print(numbers)

#계산하여 리스트에 저장
mul = [i*i for i in range(1,6) ]
print(mul)

# 조건이 있는 리스트 컴프리헨션
# 기본 형식
# [표현식 for 변수 in 반복할_데이터 if 조건식]
even_num = [i for i in range(1,11) if i % 2 == 0]
print(even_num)

#문자열을 이용
names=["김씨","이씨","빅씨"]
lengths=[len(a) for a in names]
print(lengths)

names = ["김씨", "이씨", "박씨"]
lengths = []
for a in names:
    lengths.append(len(a))
print(lengths)

#길이가 5개이상인 단어만 저장, 리스트 컴프리헨션
words=["apple","banana","kiwi","pear"]
results = [a for a in words if len(a) >= 5]
print(results)
print("단어 개수:", len(results))

# if와 else가 모두 있는 리스트 컴프리헨션
# 기본 형식
# [참일_때_값 if 조건식 else 거짓일_때_값 for 변수 in 반복할_데이터]
res= ["짝수" if i%2==0 else "홀수" for i in range(1,11)]
print(res)

#딕셔너리 컴프리헨션
# 딕셔너리는 키: 값의 형태로 저장합니다.

# 기본 형식
# {키: 값 for 변수 in 반복할_데이터}
squars={i:i*i for i in range(1,6)}
print(squars)

# 조건이 있는 컴프리헨션
#점수가 80점 이상인 학생만 저장
scores = {"김철수":85,"이영희": 70, "홍길동":90}
passs = {i:j for j,i in scores.items()}
print(passs)

listtt = [i*3 for i in range(1,11)]
print(listtt)

tyu = [i if i%3==0 else 0 for i in range(1,21)]
print(tyu)

mems = {"김철수":35,"이영희": 20, "홍길동":48}
ages = {i:j for i,j in mems.items() if j >= 30}
print(ages)
