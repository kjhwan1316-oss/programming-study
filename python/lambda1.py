# 1. 람다 함수란?
#
# 람다 함수는 "이름이 없는 짧은 함수"입니다.
# 일반 함수는 def를 사용하지만,
# 람다 함수는 lambda라는 단어를 사용합니다.
#람다 함수는 짧고 간단한 계산에 적합합니다.

# 일반 함수 형식#
# def 함수이름(매개변수):
#     return 계산식
#
# 람다 함수 형식#
# lambda 매개변수: 계산식
print("예제1. 일반 함수와 람다 함수 비교")
print("="*60)

b =lambda n : n *2

# b=double(10)
print(b(10))    

print("2제곱 람다 함수")
print("="*60)

square = lambda a : a**2
print("5의 제곱", square(5))
print("10의 제곱", square(10))

plus = lambda i,j : i+j 
mul = lambda i,j :i*j
print(plus(10,20))
print(mul(4,5))

print("조건식 람다 함수")
print("="*60)

res = lambda x : "짝수" if x % 2 == 0 else "홀수"

print(res(5))
print(res(10))

print("="*60)
print("매개변수없는 람다 함수")
h = lambda : "안녕하세요"
print(h())

gg = lambda a, b: a if a > b else b
print(gg(10,60))

print("map()과 람다함수")
# map()은 리스트의 값을 하나씩 꺼내
# 같은 계산을 반복할 때 사용합니다.
#
# 형식
# map(함수, 리스트)
#
# map()의 결과는 바로 리스트가 아니기 때문에
# list()를 사용하여 리스트로 바꿉니다.

number = [1,2,3,4,5]
result = list(map(lambda x : x*2, number))
print("원본:",number)
print("결과:",result)

print("map()으로 씩 더하기")
score = [78,89,91,56]
result_score = list(map(lambda x :x+5, score))
print(result_score)

# filter()는 조건에 맞는 값만 골라냅니다.
#
# 형식
# filter(조건 함수, 리스트)
#
# 람다 함수의 계산 결과가 True이면 남기고,
# False이면 제외합니다.
num = [10,33,45,35,26,87]
nums = list(filter(lambda x : x %3==0))
#람다함수 매개변수 x가 리스트에 한 개씩 가져오는데
#람다함수 내의 표현식이 맞으면 결과 추출
#맞지않으면 버림 -> filter
#filter,map은 결과가 list형태가 아니므로 list현태로 바꿔줘야함
print(nums)

jumsu = [45,60,90,77,55]
final_score = list(filter(lambda x : x >= 70, jumsu))
print(final_score)
