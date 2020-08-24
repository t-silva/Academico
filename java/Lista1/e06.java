import java.util.Scanner;
class e06{
	public static void main(String args[]){
		Scanner ler;
		ler = new Scanner(System.in);
		int count = 1, num;
		do{
			System.out.println("Informe o "+(count++)+"º número:");
			num = ler.nextInt();
			if (num > 0) System.out.println("Positivo");
			else if(num <0) System.out.println("Negativo");
		}while (num!=0);
	ler.close();
	}
}
