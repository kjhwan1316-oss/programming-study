#1) import calculator #.py는 쓰지않음
#2) import calculator as cal #별칭을 줌
#3) from calculator import *
from calculator import add,sub
num1 = 100
num2 = 6



#1) print("더하기:", calculator.add(num1,num2))
#1) print("빼기:", calculator.sub(num1,num2))
#2) print("곱하기:", cal.mul(num1,num2))
#3) print("나누기:", div(num1,num2))
print("더하기:", add(num1,num2))
print("빼기:", sub(num1,num2))