import java.util.Scanner;
class e02{
	public static void main(String args[]){
		Scanner ler;
		ler = new Scanner(System.in);
		System.out.println("Digite um valor para A:");
		int a = ler.nextInt();
		System.out.println("Digite um valor para B:");
		int b = ler.nextInt();
		if (a>0 && b>0){
		System.out.println("SOMA de " +a+" com "+b+" = " + (a+b));
		}
		else {
			System.out.println("Dados Inválidos");
		}
	
	}

}
