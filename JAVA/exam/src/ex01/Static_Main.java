package ex01;

class Bank{
    String owner;//멤버변수
    int balance;

    static int count = 0;//정적변수

    //생성자
    Bank(String owner, int balance){//매개변수
        this.owner = owner;
        this.balance = balance;
        count++; //객체의 관계없이 공동으로 사용
    }

    //일반 메서드
    void show(){
        System.out.println(owner+"  잔액: "+balance+"원");
        System.out.println();
    }

    static void ShowCount(){//정적메서드
        System.out.println("계좌수 : "+count);
    }
}

public class Static_Main {
    public static void main(String[] args) {
        Bank b1 = new Bank("홍길동",1000000);
        Bank b2 = new Bank("권율",3000000);
        b1.balance += 5000;
        b2.balance += 10000;
        b1.show();
        b2.show();
        //b1.count //static은 어디에도 소속되어있지않아 부를 수 럾어 오류
        //System.out.println("계좌수 : "+Bank.count);
        //static 호출: 클래스.static 이름
        Bank.ShowCount();
    }
}
