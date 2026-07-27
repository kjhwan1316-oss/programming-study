#try:
    # 혹시 오류가 있을지도 모르는 실행문
#except:
    #오류가 발생했을때 실행
#else:
    #오류가 발생하지 않을때 실행
#finally:
    #오류여부의 관계없이 무조건 실행(생략가능)
try:
    num = int(input("숫자를 입력하세요: "))
    res = 100/num
except ValueError:
    print("숫자가 아닙니다")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
except Exception as e:
    print("오류메세지", e)
else:
    print("결과는:",res)
finally:
    print("프로그램 종료")