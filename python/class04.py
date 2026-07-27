print("다중 상속과 mro")
print("\n","="*50,"\n")

class Login: #첫 번째 부모
    def run(self):
        print("run() 실행")
    def login(self):
        print("login() 실행")

class Printer: #두 번째 부모
    def run(self):
        print("Pritner클래스의 run() 실행")
    def print_info(self):
        print("프린트합니다")

class Study(Login,Printer): #자식(Login,Printer 상속받음)
    def study(self):
        print("수업중입니다")

s = Study()
s.login()
s.print_info()
s.study()
s.run()
Printer.run(s)

print("함수 탐색 순서")
print(Study.mro())
#클래스.mro(): 클래스 찾는 순서를 리스트로 보여줌
