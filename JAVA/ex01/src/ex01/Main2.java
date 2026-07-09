package ex01;

class Employee{ 
	public int pay() {
		return 0; 
	}	
}

class FullTime  extends  Employee 
   {

	@Override
	public int pay() { 	//1)
		return 5000000; 
	}
	
	public void work() {
		System.out.println("정규직 직원이 일합니다");		
	}	
}

public class Main2 {

	public static void main(String[] args) {
		
		FullTime e1  = new FullTime(); //2) 
		
		Employee p1 = new Employee(); //3)
		
		Employee  f1= new FullTime(); //4)
		
		System.out.println("부모메서드 : "+p1.pay());
		System.out.println("자식메서드: " +e1.pay());
		System.out.println("부모타입, 자식객체:다형성 " +f1.pay());
		
		e1.work();
		p1.work();
		f1.work(); //5) 오류 이유
		
		
		
	
		
		
	}

}





