print("상속, super, 오버라이딩, 다형성")
print("\n","="*50,"\n")
# 부모클래스
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def work(self):
        print(self.name, "직원이 일합니다")
    def print_info(self):
        print("이름:", self.name)
        print("급여:", self.salary,"원")
#자식클래스1
class Developer(Employee):
    def __init__(self, name, salary, language): #상속
        #부모 생성자 호출
        super().__init__(name, salary)
        self.language= language 
    #오버라이딩
    def work(self):
        print(self.name, "개발자가", self.language, "프로그램을 작성합니다")
    def print_info(self):
        super().print_info()
        print("개발언어:", self.language)
#자식클래스2
class Teacher(Employee):
    def __init__(self, name, salary, subject):
        super().__init__(name, salary)
        self.subject = subject
    def work(self):
        print(self.name,"선생님이",self.subject,"과목을 강의합니다")
    def print_info(self):
        super().print_info()
        print("교과과목:",self.subject)

d = Developer("홍길동",4500000,"파이썬")
t = Teacher("신사임당",5000000,"국사")
print("개발자정보")
d.print_info()
print("\n교사 정보")
t.print_info()

#============================================================================================
print("\n 직원들의 업무")
print("\n","="*50,"\n")

e_list = [d, t]

for e in e_list:
    e.work()
#자바의 다형성: 부모 타입-자식 객체
#파이썬의 다형성: 객체가 같은 이릉의 함수를 갖고있음 -> 실핼할 때마다 각각의 서로다른 개체의 함수가 실행
#개발자는 개발자의 work()실행, 교사는 교사의 work()실행