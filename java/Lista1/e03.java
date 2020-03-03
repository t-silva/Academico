import java.util.Scanner;
class e03{

	public static void main(String arg[]){
		Scanner ler;
		ler = new Scanner(System.in);
		System.out.println("Digite um valor para a");
		int a = ler.nextInt();
		System.out.println("Digite um valor para b");
		int b = ler.nextInt();
		if (a<0 && b <0 || a>0 && b>0)
			System.out.println("Soma de " +a+ " com " +b+ " = " + (a+b));
		else
			System.out.println("Dados Inválidos");
		

	
	}
}
