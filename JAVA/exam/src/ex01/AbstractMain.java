package ex01;

abstract class Company {
    String name;

    Company(String name) {
        this.name = name;
    }

    //공통 메서드
    void start() {
        System.out.println(name + "님이 출근했습니다");
    }

    void end() {
        System.out.println(name + "님이 퇴근했습니다");
    }

    //직무마다 다른 기능
    abstract void work();
    //추상 메서드: 내용 구현이 없음, 추상 클래스 안에 있어야함
    // 미완성, 자식드이 반드시 메서드를 완성해야함(강제성)
    //일하는 기능-직무마다 하는일이 다름
}

//자식 개발자
class Devel extends Company{//상속받음
    Devel(String name){
        super(name);
    }
    @Override
    void work(){
        System.out.println(name+"님이 프로그램을 개발합니다");
    }
}
class Designer extends Company{
    Designer(String name){
        super(name);
    }
    @Override
    void work(){
        System.out.println(name+"님이 UI를 디자인합니다");
    }
}
class Planner extends Company{
    Planner(String name){
        super(name);
    }
    @Override
    void work(){
        System.out.println(name+"님이 기획을 짭니다");
    }
}
public class AbstractMain {
    public static void main(String[] args) {
        Company c1 = new Devel("유비");
        Company c2 = new Designer("관우");
        Company c3 = new Planner("장비");

        c1.start();
        c1.work();
        c1.end();
        System.out.println();
        c2.start();
        c2.work();
        c2.end();
        System.out.println();
        c3.start();
        c3.work();
        c3.end();
        System.out.println();
    }
}
