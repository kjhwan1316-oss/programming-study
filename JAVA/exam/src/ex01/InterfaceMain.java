package ex01;

interface Login{
    void login();
    void logout();
}

interface Print{
    void printinfo();
}
//인터페이스에서 부모는 인터페이스를 사용, 자식은 클래스를 사용해 다중상속 받음
class Student implements Login, Print{
    @Override
    public void login() {
        System.out.println("학생 계정으로 로그인합니다");
    }
    @Override
    public void logout() {
        System.out.println("학생 계정에서 로그아웃힙니다");
    }
    @Override
    public void printinfo() {
        System.out.println("학생 정보를 출력합니다");
    }
}
class Teacher implements Login, Print{
    @Override
    public void login() {
        System.out.println("교사 계정으로 로그인합니다");
    }
    @Override
    public void logout() {
        System.out.println("교사 계정에서 로그아웃힙니다");
    }
    @Override
    public void printinfo() {
        System.out.println("교사 정보를 출력합니다");
    }
}
public class InterfaceMain {
    public static void main(String[] args) {
       Student s = new Student();
       Teacher t = new Teacher();
       s.login();
       s.logout();
       s.printinfo();
        System.out.println();
       t.login();
       t.logout();
       t.printinfo();
    }
}
